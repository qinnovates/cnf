// ============================================================
// EMG Subvocalization BCI — ESP32 Firmware
// ============================================================
//
// 4-channel EMG acquisition via ADS1115 (16-bit, I2C)
// Streams data over USB serial (CSV) and optional BLE
//
// Hardware:
//   ESP32 DevKit v1
//   ADS1115 breakout (I2C address 0x48)
//   4x AD620 EMG channels → ADS1115 A0-A3
//   Battery powered (3.7V LiPo → 5V boost → 3.3V reg)
//
// Wiring:
//   ADS1115 SDA → GPIO 21
//   ADS1115 SCL → GPIO 22
//   ADS1115 VDD → 3.3V
//   ADS1115 GND → GND
//   ADS1115 ADDR → GND (address 0x48)
//   ADS1115 ALRT → GPIO 4 (optional, for data-ready interrupt)
//   Status LED   → GPIO 2 (built-in on most DevKits)
//   Button       → GPIO 0 (built-in BOOT button)
//
// Modes:
//   STREAM  — continuous CSV output at sample rate
//   RECORD  — timestamped CSV with label markers (for training)
//   COMMAND — real-time classification output (after model loaded)
//
// Serial commands:
//   S — start streaming
//   X — stop streaming
//   R — enter record mode
//   L<label> — set current label (e.g., "Lyes", "Lno", "Lsilence")
//   M — mark event (insert marker in data)
//   G<gain> — set PGA gain (0=6.144V, 1=4.096V, 2=2.048V,
//             3=1.024V, 4=0.512V, 5=0.256V)
//   F<rate> — set sample rate in Hz (50-860)
//   B — toggle BLE streaming
//   ? — print status
//   H — print help
//
// Install libraries (Arduino IDE Library Manager):
//   - Adafruit ADS1X15 (by Adafruit)
//   - ArduinoJson (by Benoit Blanchon) [optional, for JSON mode]
//
// ============================================================

#include <Wire.h>
#include <Adafruit_ADS1X15.h>

// Optional: BLE support (comment out to save flash/RAM)
#define ENABLE_BLE
#ifdef ENABLE_BLE
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#endif

// ============================================================
// PIN DEFINITIONS
// ============================================================
#define PIN_SDA       21
#define PIN_SCL       22
#define PIN_ALERT     4     // ADS1115 ALRT/RDY (optional)
#define PIN_LED       2     // Built-in LED
#define PIN_BUTTON    0     // BOOT button

// ============================================================
// CONFIGURATION
// ============================================================
#define NUM_CHANNELS  4
#define I2C_CLOCK     400000  // 400kHz fast mode

// Default ADS1115 settings
// PGA gain: GAIN_ONE = ±4.096V, GAIN_TWO = ±2.048V,
//           GAIN_FOUR = ±1.024V (recommended for subvocal EMG)
adsGain_t currentGain = GAIN_FOUR;
float gainVoltage = 1.024;  // ±V range for current gain

// Sample rate (limited by ADS1115 single-ended sequential reads)
// 4 channels read sequentially: effective rate = ADS1115_rate / 4
// At 860 SPS: ~215 Hz per channel
// At 475 SPS: ~118 Hz per channel
uint16_t targetSampleRate = 200;  // Hz per channel (will round down)
uint32_t sampleIntervalUs = 5000; // microseconds between samples

// Ring buffer for smoothing serial output
#define BUFFER_SIZE 256
int16_t sampleBuffer[BUFFER_SIZE][NUM_CHANNELS];
uint32_t timestampBuffer[BUFFER_SIZE];
volatile uint16_t bufferHead = 0;
volatile uint16_t bufferTail = 0;

// ============================================================
// STATE
// ============================================================
enum Mode { MODE_IDLE, MODE_STREAM, MODE_RECORD };
Mode currentMode = MODE_IDLE;

bool bleEnabled = false;
bool bleConnected = false;
char currentLabel[32] = "silence";
uint32_t sampleCount = 0;
uint32_t startTimeMs = 0;
bool ledState = false;

// ============================================================
// OBJECTS
// ============================================================
Adafruit_ADS1115 ads;

#ifdef ENABLE_BLE
#define BLE_SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define BLE_CHAR_DATA_UUID      "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define BLE_CHAR_CONTROL_UUID   "d5875403-2945-4a30-a79e-1bfe0537b29d"

BLEServer *pServer = NULL;
BLECharacteristic *pDataChar = NULL;
BLECharacteristic *pControlChar = NULL;

class ServerCallbacks : public BLEServerCallbacks {
    void onConnect(BLEServer *server) {
        bleConnected = true;
        Serial.println("# BLE client connected");
    }
    void onDisconnect(BLEServer *server) {
        bleConnected = false;
        Serial.println("# BLE client disconnected");
        // Restart advertising
        server->startAdvertising();
    }
};

class ControlCallbacks : public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pChar) {
        String val = pChar->getValue().c_str();
        if (val.length() > 0) {
            processCommand(val.c_str()[0], val.c_str() + 1);
        }
    }
};
#endif

// ============================================================
// SETUP
// ============================================================
void setup() {
    Serial.begin(115200);
    while (!Serial && millis() < 3000) { ; }  // wait up to 3s

    pinMode(PIN_LED, OUTPUT);
    pinMode(PIN_BUTTON, INPUT_PULLUP);
    digitalWrite(PIN_LED, LOW);

    Serial.println();
    Serial.println("# ========================================");
    Serial.println("# EMG Subvocalization BCI v1.0");
    Serial.println("# 4-channel ADS1115 + ESP32");
    Serial.println("# ========================================");

    // Initialize I2C
    Wire.begin(PIN_SDA, PIN_SCL);
    Wire.setClock(I2C_CLOCK);

    // Initialize ADS1115
    if (!ads.begin(0x48, &Wire)) {
        Serial.println("# ERROR: ADS1115 not found at 0x48!");
        Serial.println("# Check wiring: SDA→GPIO21, SCL→GPIO22");
        Serial.println("# Check ADDR pin is connected to GND");
        blinkError();
        return;
    }

    ads.setGain(currentGain);
    ads.setDataRate(RATE_ADS1115_860SPS);
    Serial.println("# ADS1115 initialized (860 SPS, PGA ±1.024V)");

    // Calculate actual sample interval
    updateSampleRate(targetSampleRate);

    // Initialize BLE
    #ifdef ENABLE_BLE
    setupBLE();
    #endif

    Serial.println("# Ready. Send 'H' for help, 'S' to start.");
    Serial.println("#");
}

// ============================================================
// MAIN LOOP
// ============================================================
void loop() {
    // Handle serial commands
    while (Serial.available()) {
        char c = Serial.read();
        // Read rest of line for commands with arguments
        String arg = Serial.readStringUntil('\n');
        arg.trim();
        processCommand(c, arg.c_str());
    }

    // Handle button press (toggle stream)
    static bool lastButton = HIGH;
    bool buttonState = digitalRead(PIN_BUTTON);
    if (buttonState == LOW && lastButton == HIGH) {
        delay(50);  // debounce
        if (digitalRead(PIN_BUTTON) == LOW) {
            if (currentMode == MODE_IDLE) {
                startStream();
            } else {
                stopStream();
            }
        }
    }
    lastButton = buttonState;

    // Sample and output
    if (currentMode != MODE_IDLE) {
        acquireSample();
    }

    // Blink LED in record mode
    if (currentMode == MODE_RECORD) {
        if ((millis() / 500) % 2) {
            digitalWrite(PIN_LED, HIGH);
        } else {
            digitalWrite(PIN_LED, LOW);
        }
    }
}

// ============================================================
// DATA ACQUISITION
// ============================================================
void acquireSample() {
    static uint32_t lastSampleUs = 0;
    uint32_t now = micros();

    if (now - lastSampleUs < sampleIntervalUs) {
        return;
    }
    lastSampleUs = now;

    // Read all 4 channels sequentially
    int16_t samples[NUM_CHANNELS];
    for (int i = 0; i < NUM_CHANNELS; i++) {
        samples[i] = ads.readADC_SingleEnded(i);
    }

    uint32_t timestamp = millis() - startTimeMs;
    sampleCount++;

    // Output based on mode
    if (currentMode == MODE_STREAM) {
        outputCSV(samples, timestamp, NULL);
    } else if (currentMode == MODE_RECORD) {
        outputCSV(samples, timestamp, currentLabel);
    }

    // BLE notification
    #ifdef ENABLE_BLE
    if (bleEnabled && bleConnected) {
        sendBLE(samples, timestamp);
    }
    #endif
}

// ============================================================
// OUTPUT
// ============================================================
void outputCSV(int16_t samples[], uint32_t timestamp,
               const char *label) {
    // Format: timestamp,ch1,ch2,ch3,ch4[,label]
    Serial.print(timestamp);
    for (int i = 0; i < NUM_CHANNELS; i++) {
        Serial.print(',');
        Serial.print(samples[i]);
    }
    if (label != NULL) {
        Serial.print(',');
        Serial.print(label);
    }
    Serial.println();
}

void outputCSVHeader(bool includeLabel) {
    Serial.print("# timestamp_ms,ch1_mentalis,ch2_masseter,");
    Serial.print("ch3_submental,ch4_laryngeal");
    if (includeLabel) {
        Serial.print(",label");
    }
    Serial.println();
}

// Convert raw ADC count to voltage
float adcToVoltage(int16_t raw) {
    // ADS1115 is 16-bit signed, but single-ended reads are 15-bit
    // (0 to 32767)
    return (float)raw * gainVoltage / 32768.0;
}

// Convert voltage at ADC to estimated EMG voltage at electrode
// (divide by AD620 gain)
float adcToEMG_uV(int16_t raw, float ad620gain) {
    float v = adcToVoltage(raw);
    // Subtract Vref offset (1.65V)
    v -= 1.65;
    // Divide by gain to get original EMG signal
    return (v / ad620gain) * 1e6;  // convert to microvolts
}

// ============================================================
// BLE
// ============================================================
#ifdef ENABLE_BLE
void setupBLE() {
    BLEDevice::init("EMG-SubVocal");
    pServer = BLEDevice::createServer();
    pServer->setCallbacks(new ServerCallbacks());

    BLEService *pService = pServer->createService(BLE_SERVICE_UUID);

    // Data characteristic (notify)
    pDataChar = pService->createCharacteristic(
        BLE_CHAR_DATA_UUID,
        BLECharacteristic::PROPERTY_NOTIFY
    );
    pDataChar->addDescriptor(new BLE2902());

    // Control characteristic (write)
    pControlChar = pService->createCharacteristic(
        BLE_CHAR_CONTROL_UUID,
        BLECharacteristic::PROPERTY_WRITE
    );
    pControlChar->setCallbacks(new ControlCallbacks());

    pService->start();

    BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
    pAdvertising->addServiceUUID(BLE_SERVICE_UUID);
    pAdvertising->setScanResponse(true);
    pAdvertising->setMinPreferred(0x06);
    pAdvertising->setMinPreferred(0x12);
    BLEDevice::startAdvertising();

    Serial.println("# BLE advertising as 'EMG-SubVocal'");
}

void sendBLE(int16_t samples[], uint32_t timestamp) {
    // Pack as binary: 4 bytes timestamp + 4x 2 bytes samples = 12 bytes
    uint8_t buf[12];
    memcpy(buf, &timestamp, 4);
    for (int i = 0; i < NUM_CHANNELS; i++) {
        memcpy(buf + 4 + i * 2, &samples[i], 2);
    }
    pDataChar->setValue(buf, 12);
    pDataChar->notify();
}
#endif

// ============================================================
// COMMANDS
// ============================================================
void processCommand(char cmd, const char *arg) {
    switch (cmd) {
        case 'S': case 's':
            startStream();
            break;

        case 'X': case 'x':
            stopStream();
            break;

        case 'R': case 'r':
            startRecord();
            break;

        case 'L': case 'l':
            setLabel(arg);
            break;

        case 'M': case 'm':
            insertMarker();
            break;

        case 'G': case 'g':
            setGain(atoi(arg));
            break;

        case 'F': case 'f':
            updateSampleRate(atoi(arg));
            break;

        case 'B': case 'b':
            toggleBLE();
            break;

        case 'T': case 't':
            runSelfTest();
            break;

        case '?':
            printStatus();
            break;

        case 'H': case 'h':
            printHelp();
            break;

        case '\n': case '\r':
            break;  // ignore empty lines

        default:
            Serial.print("# Unknown command: ");
            Serial.println(cmd);
            break;
    }
}

void startStream() {
    currentMode = MODE_STREAM;
    sampleCount = 0;
    startTimeMs = millis();
    digitalWrite(PIN_LED, HIGH);
    Serial.println("# Streaming started");
    outputCSVHeader(false);
}

void startRecord() {
    currentMode = MODE_RECORD;
    sampleCount = 0;
    startTimeMs = millis();
    Serial.print("# Recording started, label: ");
    Serial.println(currentLabel);
    outputCSVHeader(true);
}

void stopStream() {
    currentMode = MODE_IDLE;
    digitalWrite(PIN_LED, LOW);
    Serial.print("# Stopped. Samples collected: ");
    Serial.println(sampleCount);

    if (sampleCount > 0) {
        uint32_t elapsed = millis() - startTimeMs;
        float actualRate = (float)sampleCount / (elapsed / 1000.0);
        Serial.print("# Actual sample rate: ");
        Serial.print(actualRate, 1);
        Serial.println(" Hz");
    }
}

void setLabel(const char *label) {
    if (strlen(label) > 0) {
        strncpy(currentLabel, label, sizeof(currentLabel) - 1);
        currentLabel[sizeof(currentLabel) - 1] = '\0';
    }
    Serial.print("# Label set: ");
    Serial.println(currentLabel);

    // Insert a label-change marker in the data stream
    if (currentMode == MODE_RECORD) {
        Serial.print("# LABEL_CHANGE,");
        Serial.println(currentLabel);
    }
}

void insertMarker() {
    uint32_t timestamp = millis() - startTimeMs;
    Serial.print("# MARKER,");
    Serial.print(timestamp);
    Serial.print(",");
    Serial.println(currentLabel);
}

void setGain(int gainIndex) {
    switch (gainIndex) {
        case 0:
            currentGain = GAIN_TWOTHIRDS;
            gainVoltage = 6.144;
            break;
        case 1:
            currentGain = GAIN_ONE;
            gainVoltage = 4.096;
            break;
        case 2:
            currentGain = GAIN_TWO;
            gainVoltage = 2.048;
            break;
        case 3:
            currentGain = GAIN_FOUR;
            gainVoltage = 1.024;
            break;
        case 4:
            currentGain = GAIN_EIGHT;
            gainVoltage = 0.512;
            break;
        case 5:
            currentGain = GAIN_SIXTEEN;
            gainVoltage = 0.256;
            break;
        default:
            Serial.println("# Invalid gain (0-5)");
            return;
    }
    ads.setGain(currentGain);
    Serial.print("# PGA gain set: +/-");
    Serial.print(gainVoltage, 3);
    Serial.println("V");
    Serial.print("# LSB size: ");
    Serial.print(gainVoltage / 32768.0 * 1e6, 2);
    Serial.println(" uV");
}

void updateSampleRate(uint16_t rate) {
    if (rate < 10) rate = 10;
    if (rate > 860) rate = 860;

    targetSampleRate = rate;
    sampleIntervalUs = 1000000 / rate;

    Serial.print("# Target sample rate: ");
    Serial.print(rate);
    Serial.println(" Hz (per channel)");

    // Note: actual rate limited by ADS1115 conversion time
    // At 860 SPS, each single-ended read takes ~1.2ms
    // 4 channels = ~4.8ms minimum = ~208 Hz max
    uint16_t maxRate = 860 / NUM_CHANNELS;
    if (rate > maxRate) {
        Serial.print("# WARNING: ADS1115 max for 4ch sequential: ~");
        Serial.print(maxRate);
        Serial.println(" Hz");
        Serial.println("# Actual rate will be lower than target");
    }
}

void toggleBLE() {
    #ifdef ENABLE_BLE
    bleEnabled = !bleEnabled;
    Serial.print("# BLE streaming: ");
    Serial.println(bleEnabled ? "ON" : "OFF");
    if (bleEnabled && !bleConnected) {
        Serial.println("# Waiting for BLE connection...");
    }
    #else
    Serial.println("# BLE not compiled (ENABLE_BLE undefined)");
    #endif
}

// ============================================================
// SELF-TEST
// ============================================================
void runSelfTest() {
    Serial.println("# ========== SELF-TEST ==========");

    // Test 1: ADS1115 communication
    Serial.print("# ADS1115 I2C (0x48): ");
    Wire.beginTransmission(0x48);
    if (Wire.endTransmission() == 0) {
        Serial.println("OK");
    } else {
        Serial.println("FAIL — check wiring");
        return;
    }

    // Test 2: Read all channels
    Serial.println("# Channel readings (raw / voltage / est. EMG uV):");
    float ad620_gain = 100.0;  // must match your RG resistor

    for (int i = 0; i < NUM_CHANNELS; i++) {
        int16_t raw = ads.readADC_SingleEnded(i);
        float voltage = adcToVoltage(raw);
        float emg = adcToEMG_uV(raw, ad620_gain);

        Serial.print("#   CH");
        Serial.print(i + 1);
        Serial.print(": raw=");
        Serial.print(raw);
        Serial.print(" voltage=");
        Serial.print(voltage, 4);
        Serial.print("V emg=");
        Serial.print(emg, 1);
        Serial.println("uV");

        // Check for issues
        if (raw <= 0) {
            Serial.print("#   WARNING: CH");
            Serial.print(i + 1);
            Serial.println(" reads 0 — input may be floating");
        }
        if (raw >= 32760) {
            Serial.print("#   WARNING: CH");
            Serial.print(i + 1);
            Serial.println(" at max — signal clipping or no connection");
        }
    }

    // Test 3: Noise floor (100 samples, compute std dev)
    Serial.println("# Noise floor test (100 samples per channel)...");
    float sum[NUM_CHANNELS] = {0};
    float sumSq[NUM_CHANNELS] = {0};
    int testSamples = 100;

    for (int s = 0; s < testSamples; s++) {
        for (int i = 0; i < NUM_CHANNELS; i++) {
            float v = adcToVoltage(ads.readADC_SingleEnded(i));
            sum[i] += v;
            sumSq[i] += v * v;
        }
    }

    for (int i = 0; i < NUM_CHANNELS; i++) {
        float mean = sum[i] / testSamples;
        float variance = (sumSq[i] / testSamples) - (mean * mean);
        float stddev = sqrt(variance);
        float noiseUv = stddev * 1e6 / 100.0;  // /gain to get input-referred

        Serial.print("#   CH");
        Serial.print(i + 1);
        Serial.print(": mean=");
        Serial.print(mean, 4);
        Serial.print("V stddev=");
        Serial.print(stddev * 1e3, 3);
        Serial.print("mV noise=");
        Serial.print(noiseUv, 1);
        Serial.println("uV (input-referred, gain=100)");
    }

    // Test 4: Sample rate benchmark
    Serial.print("# Sample rate benchmark (1000 reads)... ");
    uint32_t t0 = micros();
    for (int s = 0; s < 1000; s++) {
        ads.readADC_SingleEnded(0);
    }
    uint32_t elapsed = micros() - t0;
    float sps = 1000.0 / (elapsed / 1e6);
    Serial.print(sps, 0);
    Serial.print(" SPS single-channel, ~");
    Serial.print(sps / NUM_CHANNELS, 0);
    Serial.println(" SPS per channel (4ch sequential)");

    Serial.println("# ========== TEST COMPLETE ==========");
}

// ============================================================
// STATUS / HELP
// ============================================================
void printStatus() {
    Serial.println("# -------- Status --------");
    Serial.print("#   Mode: ");
    switch (currentMode) {
        case MODE_IDLE:   Serial.println("IDLE");    break;
        case MODE_STREAM: Serial.println("STREAM");  break;
        case MODE_RECORD: Serial.println("RECORD");  break;
    }
    Serial.print("#   Sample rate: ");
    Serial.print(targetSampleRate);
    Serial.println(" Hz");
    Serial.print("#   PGA range: +/-");
    Serial.print(gainVoltage, 3);
    Serial.println("V");
    Serial.print("#   LSB: ");
    Serial.print(gainVoltage / 32768.0 * 1e6, 2);
    Serial.println(" uV");
    Serial.print("#   Samples collected: ");
    Serial.println(sampleCount);
    Serial.print("#   Label: ");
    Serial.println(currentLabel);
    Serial.print("#   BLE: ");
    #ifdef ENABLE_BLE
    Serial.print(bleEnabled ? "ON" : "OFF");
    Serial.print(bleConnected ? " (connected)" : " (disconnected)");
    #else
    Serial.print("disabled (not compiled)");
    #endif
    Serial.println();
    Serial.print("#   Uptime: ");
    Serial.print(millis() / 1000);
    Serial.println("s");
    Serial.println("# ------------------------");
}

void printHelp() {
    Serial.println("# ======== EMG SubVocal BCI ========");
    Serial.println("# Commands:");
    Serial.println("#   S      Start streaming (CSV)");
    Serial.println("#   X      Stop streaming");
    Serial.println("#   R      Record mode (CSV + labels)");
    Serial.println("#   L<txt> Set label (e.g., Lyes Lno Lsilence)");
    Serial.println("#   M      Insert marker at current timestamp");
    Serial.println("#   G<0-5> Set PGA gain:");
    Serial.println("#          0=±6.144V 1=±4.096V 2=±2.048V");
    Serial.println("#          3=±1.024V 4=±0.512V 5=±0.256V");
    Serial.println("#   F<Hz>  Set sample rate (10-860)");
    Serial.println("#   B      Toggle BLE streaming");
    Serial.println("#   T      Run self-test");
    Serial.println("#   ?      Print status");
    Serial.println("#   H      This help");
    Serial.println("#");
    Serial.println("# Data format (stream): ms,ch1,ch2,ch3,ch4");
    Serial.println("# Data format (record): ms,ch1,ch2,ch3,ch4,label");
    Serial.println("# Lines starting with # are comments/status");
    Serial.println("#");
    Serial.println("# Button (GPIO0): toggle stream on/off");
    Serial.println("# LED (GPIO2): solid=streaming, blink=recording");
    Serial.println("# ===================================");
}

// ============================================================
// UTILITY
// ============================================================
void blinkError() {
    // Rapid blink to indicate error (never returns to normal)
    while (true) {
        digitalWrite(PIN_LED, HIGH);
        delay(100);
        digitalWrite(PIN_LED, LOW);
        delay(100);
    }
}
