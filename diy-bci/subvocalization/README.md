# DIY Subvocalization BCI — EMG Silent Speech Interface

> **Status: PROTOTYPE — Active Development**
> This is an experimental research prototype. It has NOT been peer-reviewed, certified, or validated for any clinical or commercial use. Expect rough edges, calibration challenges, and accuracy limitations. Contributions and feedback welcome.

A wearable brain-computer interface that detects silently spoken commands by reading electrical activity from your jaw, chin, and throat muscles. No implants, no surgery — just surface electrodes on skin.

**What it does:** You silently mouth a command (like "yes", "no", "go") and the device detects which word you said using muscle signals (EMG) from your face and throat.

**Inspired by:** [AlterEgo (MIT Media Lab)](https://www.media.mit.edu/projects/alterego/overview/) — which achieved 92% accuracy on ~100 internally articulated words using 7 facial electrodes.

---

## Table of Contents

- [How It Works](#how-it-works)
- [What You Need](#what-you-need)
  - [Parts to Buy](#parts-to-buy)
  - [Parts to Salvage](#parts-to-salvage)
  - [Tools Required](#tools-required)
  - [Software Requirements](#software-requirements)
- [Project Files](#project-files)
- [Step-by-Step Build Guide](#step-by-step-build-guide)
  - [Step 1: Assemble the Power Supply](#step-1-assemble-the-power-supply)
  - [Step 2: Build One EMG Channel](#step-2-build-one-emg-channel)
  - [Step 3: Test the First Channel](#step-3-test-the-first-channel)
  - [Step 4: Build All 4 Channels](#step-4-build-all-4-channels)
  - [Step 5: Wire the ADS1115 ADC to ESP32](#step-5-wire-the-ads1115-adc-to-esp32)
  - [Step 6: Flash the Firmware](#step-6-flash-the-firmware)
  - [Step 7: Verify Hardware](#step-7-verify-hardware)
  - [Step 8: Prepare Electrodes](#step-8-prepare-electrodes)
  - [Step 9: 3D Print the Chin Strap (Optional)](#step-9-3d-print-the-chin-strap-optional)
  - [Step 10: Collect Training Data](#step-10-collect-training-data)
  - [Step 11: Train the Classifier](#step-11-train-the-classifier)
  - [Step 12: Run Live Detection](#step-12-run-live-detection)
  - [Step 13: Set Up the Mobile App (Optional)](#step-13-set-up-the-mobile-app-optional)
  - [Step 14: Export Model to TensorFlow.js (Optional)](#step-14-export-model-to-tensorflowjs-optional)
- [Circuit Schematic](#circuit-schematic)
  - [Power Supply](#power-supply)
  - [Vref Generator](#vref-generator)
  - [EMG Channel (Build 4x)](#emg-channel-build-4x)
  - [AD620 Gain Resistor](#ad620-gain-resistor)
  - [Filter Component Values](#filter-component-values)
  - [ADS1115 to ESP32 Wiring](#ads1115-to-esp32-wiring)
  - [Driven Right Leg Circuit (Optional)](#driven-right-leg-circuit-optional)
- [Electrode Placement](#electrode-placement)
  - [4-Channel Configuration](#4-channel-configuration)
  - [Muscle Anatomy](#muscle-anatomy)
  - [Placement Tips](#placement-tips)
- [Software Architecture](#software-architecture)
  - [Firmware Commands](#firmware-commands)
  - [Python Companion](#python-companion)
  - [Web App Features](#web-app-features)
  - [Classification Pipeline](#classification-pipeline)
- [Calibration Guide](#calibration-guide)
  - [Choosing Command Words](#choosing-command-words)
  - [Training Session Protocol](#training-session-protocol)
  - [Improving Accuracy](#improving-accuracy)
- [Realistic Expectations](#realistic-expectations)
- [Safety](#safety)
- [Troubleshooting](#troubleshooting)
- [Science Background](#science-background)
  - [What is Subvocalization?](#what-is-subvocalization)
  - [Why EMG Works](#why-emg-works)
  - [Key Research References](#key-research-references)
- [Known Limitations](#known-limitations)
- [Future Work](#future-work)
- [License](#license)

---

## How It Works

```
    Your jaw, chin,         Analog front end         Digital
    and throat muscles      amplifies tiny           classifier
    produce electrical      muscle signals           identifies
    signals when you        and filters              which word
    silently "speak"        out noise                you said

    ┌──────────┐      ┌──────────────┐      ┌──────────────┐
    │ Ag/AgCl  │      │   AD620      │      │   ESP32      │
    │ Surface  │─────→│   ×100 gain  │─────→│   + ADS1115  │
    │ Electrode│      │   + bandpass │      │   16-bit ADC │
    └──────────┘      └──────────────┘      └──────┬───────┘
                                                    │
                                              USB or BLE
                                                    │
                                            ┌───────┴───────┐
                                            │   Python or   │
                                            │   Web App     │
                                            │               │
                                            │  Feature      │
                                            │  extraction   │
                                            │  → SVM/MLP    │
                                            │  → "YES"      │
                                            └───────────────┘
```

1. **Electrodes** on your chin, jaw, throat, and under your chin pick up microvolt-level electrical activity from muscles involved in speech
2. **Instrumentation amplifiers** (AD620) amplify these tiny signals by 100x while rejecting common-mode noise
3. **Analog filters** remove DC drift (highpass at 20 Hz) and high-frequency noise (lowpass at 500 Hz)
4. **16-bit ADC** (ADS1115) digitizes the clean signal at up to 200 Hz per channel
5. **ESP32** streams the data over USB serial or Bluetooth Low Energy (BLE)
6. **Python classifier** or **in-browser TensorFlow.js model** extracts features from 250ms signal windows and classifies them as specific commands

---

## What You Need

### Parts to Buy

| Component | Specific Part | Qty | Est. Cost | Where to Buy |
|-----------|--------------|-----|-----------|--------------|
| Instrumentation amplifier | AD620AN (DIP-8) | 4 | $20-32 | Mouser, DigiKey, Amazon |
| Dual op-amp | TL072CP (DIP-8) | 1 | $1-2 | Mouser, DigiKey, salvage |
| 16-bit ADC | ADS1115 breakout board | 1 | $3-5 | Amazon, AliExpress, Adafruit |
| Microcontroller | ESP32 DevKit v1 | 1 | $5-10 | Amazon, AliExpress |
| Gain resistor | 499Ω 1% metal film | 4 | $1 | DigiKey, Mouser |
| Resistors | 10kΩ 1/4W (assorted) | 20 | $1 | Any electronics supplier |
| Resistor | 1MΩ 1/4W | 5 | $0.50 | Any electronics supplier |
| Film capacitor | 820nF (0.82µF) polyester | 4 | $2 | Mouser, DigiKey |
| Ceramic capacitor | 33nF | 4 | $1 | Any electronics supplier |
| Ceramic capacitor | 100nF (0.1µF) | 8 | $1 | Any electronics supplier |
| Electrolytic capacitor | 10µF 25V | 4 | $1 | Any electronics supplier |
| Electrolytic capacitor | 100µF 25V | 1 | $0.50 | Any electronics supplier |
| Voltage regulator | 7805 (5V, TO-220) | 1 | $0.50 | Any electronics supplier |
| Voltage regulator | AMS1117-3.3V | 1 | $0.50 | Any electronics supplier |
| Electrodes | Ag/AgCl snap electrodes (disposable) | 100-pack | $10-15 | Amazon ("ECG electrodes") |
| Electrode cables | Snap-to-DuPont jumper leads | 4 pairs | $5-10 | Amazon, eBay |
| Battery | 9V battery + snap connector | 1 | $3 | Any store |
| Polyfuse | 500mA resettable fuse | 1 | $0.50 | Mouser, DigiKey |
| Breadboard | Full-size solderless breadboard | 1 | $5 | Amazon |
| Jumper wires | Assorted M-M, M-F | 1 pack | $3 | Amazon |
| USB cable | Micro-USB (for ESP32) | 1 | $2 | Probably already have one |
| **TOTAL** | | | **$65-95** | |

### Parts to Salvage

You can pull many of these from old electronics to reduce cost:

| Component | Salvage From |
|-----------|-------------|
| TL072 / LM358 op-amps | Old audio equipment, radios, amplifiers, CD players |
| 10kΩ, 1MΩ resistors | Any circuit board — check values with multimeter |
| 100nF, 33nF capacitors | Any circuit board |
| Shielded cable | Old 3.5mm audio cables, RCA cables (for electrode leads) |
| Elastic straps | Old headbands, swim goggles, VR headsets, sports bras |
| Velcro | Old shoes, laptop sleeves, cable organizers |
| LiPo batteries (3.7V) | Old Bluetooth speakers, earbuds, smartwatches, vape pens |
| Enclosure | Any small plastic box, mint tin, or 3D print one |
| Snap connectors | Old fitness chest straps (heart rate monitors) |

**Tip:** The AD620 instrumentation amplifier is the one component you really should buy new. It's precision analog — salvaged ones may be damaged or counterfeit.

### Tools Required

| Tool | Why |
|------|-----|
| Soldering iron + solder | For permanent connections (breadboard prototype doesn't need this) |
| Multimeter | Verify voltages, check resistor values, test continuity |
| Wire strippers | For preparing connections |
| Rubbing alcohol (isopropyl 70%+) | Cleaning skin before electrode placement |
| 3D printer (optional) | For the chin strap electrode holder |
| Computer with USB port | For programming ESP32 and running Python scripts |

### Software Requirements

**On your computer:**

```bash
# Python 3.8+ (check with: python3 --version)

# Install Python dependencies
pip install pyserial numpy scipy scikit-learn matplotlib joblib

# Optional: for TensorFlow.js model export
pip install tensorflow tensorflowjs

# Arduino IDE (for flashing ESP32 firmware)
# Download from: https://www.arduino.cc/en/software
# Then install ESP32 board package:
#   File → Preferences → Additional Board Manager URLs:
#   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
#   Then: Tools → Board → Board Manager → search "esp32" → Install

# Arduino libraries (install via Library Manager):
#   Adafruit ADS1X15 (by Adafruit)
```

**On your phone (optional):**

- Chrome browser (Android, for the BLE web app)
- On iOS: [Bluefy browser](https://apps.apple.com/app/bluefy/id1492822055) (Web Bluetooth support)

---

## Project Files

```
diy-bci/subvocalization/
├── README.md              ← You are here
├── emg_subvocal.ino       ← ESP32 Arduino firmware
├── emg_recorder.py        ← Python: record training data, train model, live detection
├── export_tfjs_model.py   ← Export trained model to TensorFlow.js format
├── emg_ble_app.html       ← BLE web app receiver with TFJS inference
└── chinstrap.scad         ← OpenSCAD 3D-printable electrode chin strap
```

| File | What It Does | When You Need It |
|------|-------------|-----------------|
| `emg_subvocal.ino` | Reads 4 EMG channels via ADS1115, streams data over USB serial and BLE | Always — this is the device firmware |
| `emg_recorder.py` | Records labeled training data, trains an SVM classifier, runs real-time command detection | Always — this is the main software |
| `export_tfjs_model.py` | Converts trained model to TensorFlow.js for in-browser inference | Only if you want to use the mobile web app for classification |
| `emg_ble_app.html` | Mobile-friendly web app that connects to ESP32 via BLE, shows live signals, runs TFJS classification | Only if you want wireless/mobile use |
| `chinstrap.scad` | Parametric 3D model for an electrode chin strap | Only if you have a 3D printer |

---

## Step-by-Step Build Guide

### Step 1: Assemble the Power Supply

The power supply converts a 9V battery into the two voltage rails needed: +5V for the analog circuits and +3.3V for the digital circuits.

**Why 9V?** The AD620 needs at least 4.6V to operate. A 9V battery provides clean, isolated power with no mains hum. A single 3.7V LiPo is too low for the AD620 without a boost converter.

**Build this on your breadboard:**

```
9V Battery (+) ──[polyfuse 500mA]──┬──[100µF electrolytic]── GND
                                   │
                              ┌────┴────┐
                              │  7805   │
                              │ IN  OUT ├── +5V rail
                              │   GND   │    ├──[100nF ceramic]── GND
                              └────┬────┘    └──[10µF electrolytic]── GND
                                   │
                                  GND

+5V rail ──┬──[100nF ceramic]── GND
           │
      ┌────┴────┐
      │AMS1117  │
      │ IN  OUT ├── +3.3V rail
      │   GND   │    ├──[100nF ceramic]── GND
      └────┬────┘    └──[10µF electrolytic]── GND
           │
          GND
```

**Verification (do this before connecting anything else):**

1. Connect the 9V battery
2. Measure voltage between +5V rail and GND with your multimeter → should read 4.9V to 5.1V
3. Measure voltage between +3.3V rail and GND → should read 3.2V to 3.4V
4. If either is wrong, check your wiring and capacitor polarity (electrolytic caps have a stripe on the negative side)

### Step 2: Build One EMG Channel

Start with a single channel to verify the circuit works before building all four. Each channel has three stages: amplification, highpass filter, and lowpass filter.

**AD620 wiring (DIP-8):**

```
Pin layout (top view, notch at left):

              ┌───────────┐
    RG ── 1  ─┤●          ├─ 8  ── RG
              │           │
   -IN ── 2  ─┤   AD620   ├─ 7  ── +5V
              │           │
   +IN ── 3  ─┤           ├─ 6  ── OUTPUT
              │           │
   GND ── 4  ─┤           ├─ 5  ── Vref (1.65V)
              └───────────┘
```

1. Insert the AD620 into your breadboard (straddle the center gap)
2. Connect pin 7 to +5V rail
3. Connect pin 4 to GND rail
4. Place a **100nF ceramic capacitor** between pin 7 and pin 4, as close to the chip as possible (this is the bypass cap — it prevents high-frequency oscillation)
5. Connect a **499Ω resistor** between pin 1 and pin 8 (this sets gain = 100)
6. Connect pin 5 (REF) to Vref (1.65V — see next section)
7. Leave pins 2 and 3 unconnected for now (these are your electrode inputs)

**Vref generator (build once, shared by all channels):**

You need a stable 1.65V reference (half of 3.3V) to center the output signal for the ADC.

```
+3.3V ──[10kΩ]──┬──[10kΩ]── GND
                │
                │  ← This is 1.65V, but too weak to drive 4 channels
                │
         TL072 pin 3 (IN+)
         TL072 pin 1 (OUT) ──→ Vref bus (connect to all AD620 pin 5)
         TL072 pin 2 (IN-) ←── TL072 pin 1 (OUT)  [feedback loop]
         TL072 pin 8 = +5V
         TL072 pin 4 = GND
         +5V ──[100nF]── GND  (near TL072 pins 8 and 4)
```

The TL072 buffer provides a low-impedance 1.65V source that won't sag under load.

**Verification:** Measure Vref with your multimeter → should read 1.60V to 1.70V.

**Highpass filter (20 Hz — blocks DC drift):**

```
AD620 pin 6 (OUTPUT) ──[820nF film cap]──┬── to lowpass
                                         │
                                      [10kΩ]
                                         │
                                       Vref (1.65V bus)
```

**Lowpass filter (500 Hz — blocks high-frequency noise):**

```
From highpass ──[10kΩ]──┬── to ADS1115 input
                        │
                     [33nF ceramic]
                        │
                       GND
```

### Step 3: Test the First Channel

Before building all four channels, verify this one works.

1. Connect pin 6 output (after the filters) to ADS1115 channel A0
2. Short AD620 pins 2 and 3 together (connect both to Vref temporarily)
3. Flash the firmware (Step 6)
4. Open Arduino serial monitor at 115200 baud
5. Send `T` to run the self-test
6. You should see the channel reading near the midpoint (~16000-17000 for single-ended)
7. The value should be stable with low noise (std dev < 50)
8. Now disconnect the short and touch pin 2 and pin 3 with your fingers — you should see 50/60 Hz noise (large oscillations). This confirms the amplifier is alive.

**If the output is stuck at 0 or 32767:** Check that pin 5 is connected to Vref (not GND), check the bypass cap is present, and check the gain resistor is between pins 1 and 8.

### Step 4: Build All 4 Channels

Repeat the AD620 + filter circuit three more times. Each channel is identical.

Use the same Vref bus for all four AD620 REF pins (pin 5).

**Layout tip:** Place the four AD620s in a row on the breadboard. Run the +5V, GND, and Vref buses along the power rails. Keep the filter components close to each AD620 to minimize noise pickup.

```
Breadboard layout (approximate):

+5V rail ─────────────────────────────────────────
GND rail ─────────────────────────────────────────

  [AD620 #1]    [AD620 #2]    [AD620 #3]    [AD620 #4]
  + filters     + filters     + filters     + filters
      │              │              │              │
      A0             A1             A2             A3
              ┌──────────────┐
              │   ADS1115    │
              └──────┬───────┘
                     │ I2C
              ┌──────┴───────┐
              │    ESP32     │
              └──────────────┘

[TL072] ── Vref bus to all AD620s
```

### Step 5: Wire the ADS1115 ADC to ESP32

```
ADS1115 Breakout          ESP32 DevKit
─────────────────         ────────────
VDD ──────────────────── 3.3V
GND ──────────────────── GND
SDA ──────────────────── GPIO 21
SCL ──────────────────── GPIO 22
ADDR ─────────────────── GND          (sets I2C address to 0x48)
A0 ───────────────────── CH1 filter output (Mentalis)
A1 ───────────────────── CH2 filter output (Masseter)
A2 ───────────────────── CH3 filter output (Submental)
A3 ───────────────────── CH4 filter output (Laryngeal)
```

**I2C pull-up resistors:** Most ADS1115 breakout boards include 10kΩ pull-ups on SDA and SCL. If yours doesn't, add **4.7kΩ pull-ups** from SDA to 3.3V and from SCL to 3.3V.

**Important:** The ADS1115 runs on 3.3V (same as ESP32), so its analog inputs can safely accept 0-3.3V signals. The AD620 output centered at Vref (1.65V) will swing within this range for normal EMG signals.

### Step 6: Flash the Firmware

1. Open `emg_subvocal.ino` in Arduino IDE
2. Select board: **Tools → Board → ESP32 Dev Module**
3. Select port: **Tools → Port → /dev/tty.usbserial-XXXX** (macOS) or **COMx** (Windows)
4. Upload settings:
   - Upload Speed: **921600**
   - Flash Frequency: **80MHz**
   - Partition Scheme: **Default 4MB with spiffs**
5. Click **Upload** (→ button)
6. Wait for "Done uploading" message
7. Open **Serial Monitor** (magnifying glass icon), set baud rate to **115200**
8. You should see:

```
# ========================================
# EMG Subvocalization BCI v1.0
# 4-channel ADS1115 + ESP32
# ========================================
# ADS1115 initialized (860 SPS, PGA ±1.024V)
# Target sample rate: 200 Hz (per channel)
# BLE advertising as 'EMG-SubVocal'
# Ready. Send 'H' for help, 'S' to start.
```

If you see `# ERROR: ADS1115 not found at 0x48!` — check your I2C wiring (SDA to GPIO 21, SCL to GPIO 22) and that the ADDR pin is connected to GND.

### Step 7: Verify Hardware

Send `T` in the serial monitor to run the self-test:

```
# ========== SELF-TEST ==========
# ADS1115 I2C (0x48): OK
# Channel readings (raw / voltage / est. EMG uV):
#   CH1: raw=16234 voltage=0.5081V emg=23.4uV
#   CH2: raw=16201 voltage=0.5071V emg=18.7uV
#   CH3: raw=16298 voltage=0.5101V emg=31.2uV
#   CH4: raw=16187 voltage=0.5066V emg=15.9uV
# Noise floor test (100 samples per channel)...
#   CH1: mean=0.5082V stddev=0.312mV noise=3.1uV
#   CH2: mean=0.5070V stddev=0.287mV noise=2.9uV
#   CH3: mean=0.5098V stddev=0.345mV noise=3.5uV
#   CH4: mean=0.5065V stddev=0.298mV noise=3.0uV
# Sample rate benchmark: 847 SPS single-channel, ~211 SPS per ch
# ========== TEST COMPLETE ==========
```

**What to check:**
- All channels should show raw values in the 14000-18000 range (centered near Vref)
- Noise floor should be < 10 µV input-referred (noise column)
- Any channel reading 0 or 32767 has a wiring problem
- Sample rate should be > 200 SPS single-channel

### Step 8: Prepare Electrodes

**Using disposable Ag/AgCl snap electrodes (recommended for starting):**

1. Clean target skin areas with rubbing alcohol, let dry
2. If you have hairy skin at electrode sites, consider shaving the area (hair increases impedance)
3. Peel off electrode backing and press firmly onto skin
4. Connect snap-to-DuPont cables to electrodes
5. Connect DuPont ends to AD620 inputs (pin 2 = negative, pin 3 = positive)

**Electrode impedance check:** With electrodes on skin, measure resistance between the two electrodes of a pair with your multimeter. Should be **< 20 kΩ**. If higher, press electrodes more firmly, clean skin again, or try a different location with less hair.

### Step 9: 3D Print the Chin Strap (Optional)

If you have a 3D printer, use `chinstrap.scad` to print a custom electrode holder.

**Setup:**

```bash
# Install OpenSCAD (free)
brew install openscad    # macOS
# or download from https://openscad.org/downloads.html
```

**Customize for your face:**

Open `chinstrap.scad` and measure yourself with a flexible tape measure:

```openscad
chin_width = 55;            // Widest point of your jawline (mm)
chin_to_ear = 130;          // Chin tip to front of ear hole (mm)
chin_to_throat = 90;        // Under chin to Adam's apple (mm)
ear_to_ear_over_head = 340; // Ear-to-ear arc over top of head (mm)
```

**Preview:** Open in OpenSCAD, press F5 to preview the assembly.

**Export STLs:** Comment out `assembly();`, uncomment individual parts (e.g., `chin_cradle();`), press F6 to render, then File → Export → STL.

**Print settings:**

| Part | Material | Layer | Infill | Supports |
|------|----------|-------|--------|----------|
| Chin cradle | TPU 95A | 0.2mm | 15% | No |
| Jaw arms | PLA | 0.2mm | 20% | Where needed |
| Throat arm | TPU 95A | 0.2mm | 15% | No |
| Ear hooks | TPU 95A | 0.2mm | 15% | No |
| Electronics box | PLA | 0.2mm | 20% | Yes |

**No 3D printer? Quick alternative:**
1. Buy a cycling chin strap (~$5)
2. Hot-glue or sew electrode snap buttons at the 4 positions
3. Route wires along the strap with tape
4. Tuck electronics in a shirt pocket

### Step 10: Collect Training Data

This is the most important step. The classifier is only as good as your training data.

**Find your serial port:**

```bash
# macOS
ls /dev/tty.usb*

# Linux
ls /dev/ttyUSB*

# Windows
# Check Device Manager → Ports (COM & LPT)

# Cross-platform
python3 -m serial.tools.list_ports
```

**Edit the port in `emg_recorder.py`:**

Open `emg_recorder.py` and change the `SERIAL_PORT` line near the top:

```python
SERIAL_PORT = "/dev/tty.usbserial-0001"  # ← Change this to your port
```

**Run the hardware test first:**

```bash
python3 emg_recorder.py test --port /dev/tty.usbserial-XXXX
```

You should see all 4 channels responding. Clench your jaw — CH2 (masseter) should show a large spike.

**Collect training data:**

```bash
python3 emg_recorder.py calibrate --port /dev/tty.usbserial-XXXX
```

The script will guide you through a calibration session:

```
==================================================
  EMG SUBVOCALIZATION CALIBRATION
==================================================
  Commands: ['yes', 'no', 'go', 'stop', 'select']
  Reps per command: 25
  Trial duration: 2.0s
  Rest between trials: 2.0s

  Press ENTER when electrodes are placed and ready...

--------------------------------------------------
  BASELINE: Relax jaw completely. No speaking.
--------------------------------------------------
  Press ENTER when ready for 'silence'...
  Trial  1/25: 3...2...1...GO! (387 samples)
  Trial  2/25: 3...2...1...GO! (391 samples)
  ...
```

**During calibration:**
- For **silence** trials: relax completely, jaw loose, eyes forward
- For **command** trials: silently mouth the word with exaggerated lip/jaw movement
- Be **consistent** — say each word the same way every time
- If you mess up a trial, keep going — a few bad trials won't ruin the model
- The session takes about 20 minutes

**Custom commands:**

```bash
# Use your own command words
python3 emg_recorder.py calibrate --commands up down left right click

# Change repetition count (more = better accuracy, longer session)
python3 emg_recorder.py calibrate --reps 30
```

**Output:** Training data is saved to `emg_data/training_YYYYMMDD_HHMMSS.csv`

### Step 11: Train the Classifier

```bash
python3 emg_recorder.py train
```

The script will:
1. Load the most recent training data file
2. Preprocess (bandpass filter + notch filter)
3. Extract 8 features × 4 channels = 32 features per window
4. Train an SVM classifier with 5-fold cross-validation
5. Print accuracy and confusion matrix
6. Save the model to `subvocal_model.pkl`

**Example output:**

```
Loading emg_data/training_20260204_103000.csv...
  Loaded 19500 samples, 6 classes
Preprocessing...
Extracting features...
  Feature matrix: 776 windows x 32 features
  Class distribution:
    go: 125 windows
    no: 131 windows
    select: 128 windows
    silence: 130 windows
    stop: 127 windows
    yes: 135 windows

Training SVM (RBF kernel)...

  Cross-validation accuracy: 82.3% (+/- 4.1%)
  Per-fold: 78.1%, 84.5%, 80.6%, 86.2%, 82.1%

Model saved: subvocal_model.pkl
Scaler saved: subvocal_scaler.pkl
```

**If accuracy is below 60%:**
- Collect more training data (50 reps instead of 25)
- Use more distinct command words (see [Choosing Command Words](#choosing-command-words))
- Check electrode contact — clean skin, press firmly
- Make sure you're exaggerating the mouth movements during calibration

### Step 12: Run Live Detection

```bash
python3 emg_recorder.py live --port /dev/tty.usbserial-XXXX
```

**Output:**

```
==================================================
  LIVE DETECTION — Listening for commands...
  Press Ctrl+C to stop
==================================================

  ... listening  (noise: 0.12)
  ... listening  (noise: 0.15)
  >> YES  (confidence: 80%, probability: 0.73)
    → Action: CONFIRM
  ... listening  (noise: 0.11)
  >> STOP  (confidence: 100%, probability: 0.89)
    → Action: PAUSE
```

**Customize actions:** Edit the `command_callback` function at the bottom of `emg_recorder.py` to map commands to keyboard shortcuts, smart home controls, or anything else:

```python
def command_callback(command, confidence):
    # Example: keyboard simulation
    import pyautogui
    key_map = {"yes": "enter", "no": "escape", "go": "right",
               "stop": "space", "select": "return"}
    if command in key_map:
        pyautogui.press(key_map[command])
```

### Step 13: Set Up the Mobile App (Optional)

The BLE web app lets you view signals and detect commands wirelessly on your phone.

1. **Enable BLE on ESP32:** Open serial monitor, type `B` then `S` (enables BLE + starts streaming)
2. **Open the web app:** Open `emg_ble_app.html` in Chrome on your phone/computer
3. **Connect:** Tap "CONNECT TO DEVICE", select "EMG-SubVocal" from the Bluetooth dialog
4. **View signals:** You should see live waveforms for all 4 channels
5. **Test classification:** Tap "Classify" — the built-in threshold classifier will respond to jaw clenches

**For ML classification on mobile:** See Step 14 to export your trained model to TensorFlow.js.

### Step 14: Export Model to TensorFlow.js (Optional)

This converts your trained Python model into a format that runs in the web browser.

```bash
# Install TensorFlow and TF.js converter
pip install tensorflow tensorflowjs

# Option A: Train a fresh Keras model (recommended)
python3 export_tfjs_model.py train

# Option B: Distill your existing SVM into a neural network
python3 export_tfjs_model.py distill
```

**Output:** `tfjs_model/` directory containing the model files.

**Load in the web app:**
1. Open `emg_ble_app.html` in Chrome
2. In the "ML Model" panel, tap "Load Model Folder"
3. Select the `tfjs_model/` directory
4. The badge changes from THRESHOLD (orange) to TFJS (green)
5. Tap "Classify" — now using your trained model in-browser

**Serving from a URL:** If you want to host the model:

```bash
# Start a local server in the project directory
cd diy-bci/subvocalization
python3 -m http.server 8080

# In the web app, tap "Load from URL" and enter:
# http://localhost:8080/tfjs_model/model.json
```

---

## Circuit Schematic

### Power Supply

```
9V Battery ──[F1 500mA polyfuse]──┬──[C1 100µF]── GND
                                  │
                             ┌────┴────┐
                             │  7805   │
                             │ IN  OUT ├── +5V
                             │   GND   │    ├──[C2 100nF]── GND
                             └────┬────┘    └──[C3 10µF]── GND
                                  │
                                 GND

+5V ──┬──────────────────────────────
      │
 ┌────┴────┐
 │AMS1117  │
 │ IN  OUT ├── +3.3V
 │   GND   │    ├──[C4 100nF]── GND
 └────┬────┘    └──[C5 10µF]── GND
      │
     GND
```

### Vref Generator

```
+3.3V ──[R1 10kΩ]──┬──[R2 10kΩ]── GND
                    │
                    └── TL072A pin 3 (+IN)
                        TL072A pin 1 (OUT) ──── Vref (1.65V bus)
                        TL072A pin 2 (-IN) ←─── TL072A pin 1  [feedback]
                        TL072 pin 8 = +5V ──[C7 100nF]── pin 4 = GND
                        Vref bus ──[C6 10µF]── GND
```

### EMG Channel (Build 4x)

```
                                              +5V
                                               │
Electrode (+) ── pin 3 (+IN)            pin 7 (V+)
                              ┌────────────────┤
Electrode (-) ── pin 2 (-IN) │     AD620      │
                              │                 │ pin 6 (OUT)
                              │ pin 1 ─[RG]─ pin 8    │
                              │                 │      │
                        GND ─ pin 4 (V-)       │  HIGHPASS (20Hz)
                              │                 │      │
                     Vref ── pin 5 (REF)       │  ──[C8 820nF]──┬── LOWPASS
                              └────────────────┘               │
                                                            [R3 10kΩ]
                              [C_byp 100nF]                    │
                              between pin 7                  Vref
                              and pin 4
                                                          LOWPASS (500Hz)
                                                               │
                                                          ──[R4 10kΩ]──┬── ADS1115
                                                                       │
                                                                    [C9 33nF]
                                                                       │
                                                                      GND
```

### AD620 Gain Resistor

| Desired Gain | RG Value | When to Use |
|-------------|----------|-------------|
| 50 | 1.02 kΩ | If signals are clipping (too large) |
| **100** | **499 Ω** | **Default — start here** |
| 200 | 249 Ω | If signals are too small |
| 500 | 100 Ω | For very weak subvocalization signals |

Formula: `Gain = 1 + (49.4 kΩ / RG)`

Use 1% tolerance metal film resistors for accurate, stable gain.

### Filter Component Values

**Highpass (removes DC drift, passes EMG above 20 Hz):**

| Component | Value | Cutoff Frequency |
|-----------|-------|-----------------|
| C8 | 820 nF polyester film | fc = 1/(2π × 10k × 820n) = 19.4 Hz |
| R3 | 10 kΩ | (bias to Vref) |

**Lowpass (removes noise above 500 Hz):**

| Component | Value | Cutoff Frequency |
|-----------|-------|-----------------|
| R4 | 10 kΩ | fc = 1/(2π × 10k × 33n) = 482 Hz |
| C9 | 33 nF ceramic | |

These are first-order filters (20 dB/decade rolloff). For a steeper rolloff, you can cascade two stages per filter, but first-order is sufficient for a prototype.

### ADS1115 to ESP32 Wiring

```
ADS1115            ESP32
────────           ─────
VDD ────────────── 3.3V
GND ────────────── GND
SDA ────────────── GPIO 21
SCL ────────────── GPIO 22
ADDR ───────────── GND         (I2C address 0x48)
A0 ─────────────── CH1 output  (Mentalis)
A1 ─────────────── CH2 output  (Masseter)
A2 ─────────────── CH3 output  (Submental)
A3 ─────────────── CH4 output  (Laryngeal)
```

**ADS1115 PGA gain settings** (configured in firmware, adjustable via serial command `G<0-5>`):

| Setting | Range | Resolution (LSB) | Best For |
|---------|-------|----------|---------|
| G0 | ±6.144V | 187.5 µV | Testing/debug |
| G1 | ±4.096V | 125 µV | Large signals |
| G2 | ±2.048V | 62.5 µV | General use |
| **G3** | **±1.024V** | **31.25 µV** | **Subvocalization (default)** |
| G4 | ±0.512V | 15.6 µV | Very weak signals |
| G5 | ±0.256V | 7.8 µV | Minimum noise floor |

### Driven Right Leg Circuit (Optional)

Improves signal-to-noise ratio by actively cancelling 50/60 Hz powerline interference. Worth adding if you're in a noisy electrical environment.

```
CH1 output ──[R5 1MΩ]──┐
CH2 output ──[R6 1MΩ]──┤
CH3 output ──[R7 1MΩ]──┼── Summing point ── TL072B pin 6 (-IN)
CH4 output ──[R8 1MΩ]──┘
                                              TL072B pin 5 (+IN) ── Vref
                        ┌── [R10 100kΩ] ──── TL072B pin 6 (-IN)
                        │
                TL072B pin 7 (OUT)
                        │
                     [R9 1MΩ]   ← SAFETY resistor (limits current to <5µA)
                        │
                   DRL ELECTRODE  (place on mastoid bone, behind ear)
```

---

## Electrode Placement

### 4-Channel Configuration

```
        ┌─────────────────┐
        │    FOREHEAD      │ ← REF/GND (bony, minimal muscle)
        │                  │
        │   ┌──────────┐   │
        │   │   NOSE   │   │
        │   └──────────┘   │
        │                  │
        │ [CH2]      [CH2] │ ← Masseter (clench jaw to find it)
        │  L            R  │
        └────────┬─────────┘
            [CH1]           ← Mentalis (chin, just below lower lip)
                │
            [CH3]           ← Submental (directly under chin, midline)
                │
            [CH4]           ← Laryngeal (side of throat, beside Adam's apple)
```

| Channel | Muscle | Location | What It Detects |
|---------|--------|----------|-----------------|
| CH1 | Mentalis | Chin, just below the center of your lower lip | Lip closure — sounds like M, B, P |
| CH2 | Masseter | Cheek, over the jaw angle (clench teeth to feel it bulge) | Jaw clenching — vowel shaping, jaw position |
| CH3 | Digastric / Mylohyoid | Directly under the chin, midline (tip your head back to feel the soft area) | Tongue movement — jaw opening, tongue elevation |
| CH4 | Thyrohyoid | Side of the throat, next to the Adam's apple | Larynx movement — voicing, swallowing |
| REF | — | Mastoid bone (behind ear) or center of forehead | Reference — low muscle activity area |

### Muscle Anatomy

**Why these muscles?** When you silently speak, the same muscles activate as during regular speech — just at a much lower intensity. The four muscles above cover the major articulators:

- **Mentalis** → lips (labial consonants: p, b, m)
- **Masseter** → jaw (vowel height: open/close)
- **Digastric** → tongue (lingual consonants: t, d, l, n)
- **Thyrohyoid** → larynx (voiced vs. unvoiced, pitch)

Research reference: [AlterEgo (MIT, Kapur et al. 2018)](https://www.media.mit.edu/projects/alterego/overview/) tested 16 electrode positions and found 7 optimal locations along the jaw and mouth. They later showed 4 electrodes along a single jaw achieved comparable results.

### Placement Tips

1. **Clean the skin** with rubbing alcohol before placing electrodes
2. **Shave** if there's hair at the electrode site (reduces impedance by 5-10x)
3. **Press firmly** for 5-10 seconds after placing each electrode
4. **Check impedance** with a multimeter: < 20 kΩ between electrode pairs
5. **Mark positions** with a skin-safe marker so you can replicate placement across sessions (placement consistency is the #1 factor in cross-session accuracy)
6. **Bipolar pairs:** Each channel uses two electrodes ~2 cm apart, oriented along the muscle fiber direction
7. **Reference electrode:** Place on a bony prominence (behind ear or center of forehead) where there's minimal muscle activity

---

## Software Architecture

### Firmware Commands

Send these via Serial Monitor (115200 baud) or BLE control characteristic:

| Command | Action | Example |
|---------|--------|---------|
| `S` | Start streaming data (CSV format) | `S` |
| `X` | Stop streaming | `X` |
| `R` | Record mode (adds label column) | `R` |
| `L<word>` | Set current label for recording | `Lyes`, `Lsilence` |
| `M` | Insert timestamp marker in data | `M` |
| `G<0-5>` | Set ADC PGA gain | `G3` (±1.024V) |
| `F<Hz>` | Set sample rate | `F200` |
| `B` | Toggle BLE data streaming | `B` |
| `T` | Run hardware self-test | `T` |
| `?` | Print current status | `?` |
| `H` | Print help | `H` |

**Data format (stream mode):** `timestamp_ms,ch1,ch2,ch3,ch4`
**Data format (record mode):** `timestamp_ms,ch1,ch2,ch3,ch4,label`
**Comment lines** start with `#` and are ignored by the Python scripts.

**Hardware button:** GPIO 0 (BOOT button on ESP32 DevKit) toggles streaming on/off.
**LED:** GPIO 2 — solid = streaming, blinking = recording.

### Python Companion

```bash
python3 emg_recorder.py <command> [options]

Commands:
  test           Run hardware self-test, verify electrode contact
  calibrate      Guided training data collection session
  train          Train SVM classifier from recorded data
  live           Real-time command detection
  plot           Live signal visualization (matplotlib)
  plot-training  Visualize recorded training data by label

Options:
  --port PORT        Serial port (default: see SERIAL_PORT in script)
  --commands W1 W2   Custom command words for calibration
  --reps N           Repetitions per command (default: 25)
  --data FILE        Specific training data file to use
```

### Web App Features

| Feature | Description |
|---------|-------------|
| BLE connect | Pairs with ESP32 "EMG-SubVocal" device via Web Bluetooth |
| Live waveforms | 4-channel canvas rendering at 60fps with auto-scaling |
| Threshold classifier | Built-in RMS-based activity detector (no model needed) |
| TFJS classifier | Load a trained TensorFlow.js model for real ML inference |
| Probability bars | Per-class softmax probabilities in real-time |
| Record | Buffer EMG samples with timestamps |
| Export CSV | Download recorded data as a CSV file |
| Freeze | Pause waveform display for inspection |
| Gain control | Send PGA gain changes to ESP32 via BLE |
| Command history | Scrolling list of detected commands with timestamps |
| Haptic feedback | Vibration on Android when a command is detected |

**Keyboard shortcuts:** Space=connect, R=record, F=freeze, C=classify, E=export, M=load model

### Classification Pipeline

The same feature extraction pipeline runs in both Python and JavaScript:

```
Raw ADC samples (200 Hz, 4 channels)
    │
    ▼
IIR Notch filter (60 Hz, removes powerline noise)
    │
    ▼
Butterworth bandpass (20-100 Hz, isolates EMG band)
    │
    ▼
Sliding window (250ms, 50% overlap)
    │
    ▼
Feature extraction (8 features × 4 channels = 32 total):
    ├── MAV   (Mean Absolute Value)
    ├── RMS   (Root Mean Square)
    ├── WL    (Waveform Length)
    ├── VAR   (Variance)
    ├── IEMG  (Integrated EMG)
    ├── ZC    (Zero Crossings)
    ├── SSC   (Slope Sign Changes)
    └── AAC   (Average Amplitude Change)
    │
    ▼
StandardScaler normalization (zero mean, unit variance)
    │
    ▼
Classifier (SVM in Python, or MLP in TensorFlow.js)
    │
    ▼
Majority vote (over 5-7 consecutive predictions)
    │
    ▼
Output: command + confidence
```

---

## Calibration Guide

### Choosing Command Words

Words with **different jaw/lip/tongue positions** are easier to distinguish. Words that sound similar will confuse the classifier.

**Good command sets (high distinctiveness):**

| Set | Words | Why It Works |
|-----|-------|-------------|
| Navigation | up, down, left, right, click | Different jaw heights and tongue positions |
| Binary + | yes, no, select | Very distinct lip/jaw shapes |
| Control | go, stop, pause, next | Different initial consonants |
| Media | play, skip, mute, louder | Varied lip rounding and jaw opening |

**Bad command sets (too similar):**

| Words | Problem |
|-------|---------|
| go, no, so, low | All end in "o", differ only in initial consonant |
| bit, bet, bat, bot | Minimal jaw/lip difference |
| one, two, three, four | Numbers have subtle articulatory differences |

**Rule of thumb:** Say each word aloud and watch your jaw in a mirror. If two words look the same, they'll be hard to classify from EMG.

### Training Session Protocol

1. **Warmup (2 min):** Practice silently mouthing each command word 5 times. Exaggerate the movements. Get comfortable with the rhythm.

2. **Baseline (5 min):** The script records 25 trials of silence. Stay relaxed. Don't clench your jaw, don't swallow, don't look around.

3. **Commands (3-4 min per command):** The script prompts each command. Wait for "GO!", then silently mouth the word with exaggerated lip/jaw movement for 2 seconds. Rest for 2 seconds. Repeat 25 times.

4. **Post-check:** After training, the script reports per-class accuracy. If any command is below 60%, re-record that command with more deliberate articulation.

**Tips for better data:**
- **Hyperarticulate:** Move your jaw and lips more than feels natural. You can reduce movement later once the model works.
- **Be consistent:** Say each word the exact same way every time. Consistency > naturalness.
- **Don't move your head:** Keep your head still during trials. Head movement causes electrode motion artifacts.
- **Stay hydrated:** Dry mouth changes your articulation patterns.
- **Take breaks:** After 50 trials, rest for 2-3 minutes. Muscle fatigue changes EMG patterns.

### Improving Accuracy

| Problem | Solution |
|---------|----------|
| Overall accuracy < 60% | Collect more data (50+ reps), use more distinct words |
| One class always confused with another | Replace the confused word with something more distinct |
| Accuracy drops across sessions | Mark electrode positions with skin marker, recalibrate each session |
| High accuracy on mouthed speech, low on subvocalization | This is normal — start with mouthed speech, gradually reduce movement over weeks |
| Classifier predicts one class too often | Class imbalance — ensure equal reps for all classes including silence |
| Noisy signals (spiky waveforms) | Check electrode contact, reduce cable movement, move away from power sources |

---

## Realistic Expectations

This is a prototype. Be honest with yourself about what to expect:

| Mode | Commands | Accuracy | Notes |
|------|----------|----------|-------|
| **Mouthed speech** (exaggerated) | 3-5 | 85-95% | Start here |
| **Quiet mouthing** (minimal visible movement) | 3-5 | 70-85% | Achievable with practice |
| **True subvocalization** (no visible movement) | 3-5 | 55-75% | Hardest, requires many sessions |
| **True subvocalization** | 10+ words | 40-65% | Accuracy degrades rapidly with vocabulary |

**What works well:**
- Binary classification (yes vs. no vs. silence) — 85-95%
- Commands with very different jaw positions
- Consistent electrode placement
- Patient calibration with many repetitions

**What is hard:**
- True silent inner speech with zero visible movement
- Cross-session generalization (accuracy drops 20-25% when you re-place electrodes)
- Similar-sounding words
- Continuous speech recognition (this system does isolated word/command detection only)
- Using the system while walking, talking, or eating

---

## Safety

**CRITICAL SAFETY RULES:**

1. **BATTERY POWER ONLY.** Never connect the device to mains power (wall outlet) while wearing it. This eliminates all risk of dangerous current flowing through your body.

2. **If using USB:** Keep the laptop on battery power too, or use a USB isolator (~$15 on Amazon). A laptop plugged into a wall outlet creates a path from mains AC through the laptop, through USB, through the device, through you, to ground.

3. **Never charge batteries while wearing the device.** Remove it first, then charge.

4. **The polyfuse is non-negotiable.** The 500mA resettable fuse on the battery output limits worst-case current. Do not bypass it.

5. **If you feel tingling, remove the device immediately.** Check for shorts with a multimeter.

6. **Do not use if you have a pacemaker or any implanted electronic medical device.** Even microcurrents could interfere with implant function.

7. **Do not use near water** (shower, pool, rain).

8. **This is NOT a medical device.** It has not been tested or certified under IEC 60601-1, FDA regulations, or any other medical device standard. Do not use it for medical diagnosis, treatment, or any clinical purpose. **Use at your own risk.**

**Why these rules matter:** The IEC 60601-1 standard limits current through the body to 100 µA for body-contact devices and 10 µA for cardiac-contact devices. Your AD620 circuit, if shorted to a mains-connected source, could deliver milliamps — 100x the safety limit. Battery isolation makes this impossible.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `ADS1115 not found at 0x48` | I2C wiring wrong | Check SDA→GPIO21, SCL→GPIO22, ADDR→GND |
| Channel reads 0 constantly | AD620 not powered, or input floating | Check +5V on pin 7, GND on pin 4, bypass cap present |
| Channel reads 32767 constantly | Signal clipping (too high) | Lower gain (change RG to 1kΩ), or check Vref connection to pin 5 |
| All channels show same value | All inputs shorted together | Check breadboard connections, ensure each AD620 has separate inputs |
| Massive 50/60 Hz noise | Powerline interference | Move away from power cables, add DRL circuit, use shielded cables |
| Signal drifts slowly up/down | DC offset leaking through highpass | Check C8 (820nF) is connected, check R3 goes to Vref not GND |
| No BLE device found | BLE not enabled on ESP32 | Send `B` via serial to enable, then `S` to start streaming |
| Web app says "not supported" | Wrong browser | Use Chrome (not Safari or Firefox) |
| Python can't open serial port | Wrong port name or port in use | Check port with `ls /dev/tty.usb*`, close Arduino Serial Monitor |
| Training accuracy < 40% | Bad electrode contact or wrong placement | Re-clean skin, check impedance < 20kΩ, verify placement per diagram |
| Model works in lab, fails on desk | Electrode position shifted | Mark positions with skin marker, recalibrate after every re-donning |
| ESP32 keeps resetting | Power supply issue | Check 9V battery voltage (replace if < 7V), check regulator output |

---

## Science Background

### What is Subvocalization?

Subvocalization is the internal speech process that occurs when you "talk to yourself" silently. When you read, think, or mentally rehearse words, the muscles involved in speech production activate at low levels — even though you don't produce audible sound.

This has been known since the 1800s. In 1899, psychologist E.B. Huey observed that "the organs of speech always have some part in inner speech." Modern EMG studies confirm that subvocalization produces measurable electrical activity in the perioral (around-mouth), submental (under-chin), and laryngeal (throat) muscles.

The signal is weak — typically 10-100x smaller than active speech EMG — but with sensitive amplification and machine learning, it can be decoded into discrete commands.

### Why EMG Works

| Property | Value | Why It Matters |
|----------|-------|---------------|
| EMG signal amplitude | 50 µV - 5 mV (surface EMG) | Detectable with instrumentation amplifiers |
| Subvocalization amplitude | 5 - 500 µV | Requires high-gain, low-noise amplification |
| EMG frequency band | 20 - 500 Hz | Well-separated from most electrical noise |
| Subvocalization band | 20 - 200 Hz (mostly < 100 Hz) | Narrower band, focused filtering helps |
| Muscle activation patterns | Different for each phoneme | Enables word-level classification |
| Electrode spacing | ~2 cm (bipolar) | Localizes signal to specific muscle |

### Key Research References

1. **Kapur, A., Kapur, S., and Maes, P.** (2018). "AlterEgo: A Personalized Wearable Silent Speech Interface." *Proceedings of the 23rd International Conference on Intelligent User Interfaces (IUI '18)*, pp. 43-53. — 92% accuracy on ~100 internally articulated words with 7 facial electrodes.

2. **Meltzner, G.S., et al.** (2017). "Silent Speech Recognition as an Alternative Communication Device for Persons with Laryngectomy." *IEEE/ACM Transactions on Audio, Speech, and Language Processing.* — NASA/Delsys approach to silent speech EMG.

3. **MDPI Sensors** (2025). "Electrode Setup for EMG-Based Silent Speech Interfaces: A Pilot Study." *Sensors, 25(3), 781.* — Optimal electrode placement study, 8 channels, 89.6% word accuracy.

4. **Mateus Aquino.** [subvocalization-emg](https://github.com/MateusAquino/subvocalization-emg) — Open-source subvocalization project using OpenBCI Cyton, 8-channel montage.

5. **Phan et al.** (2025). "EMG sensor with DRL circuit for improved SNR." *Journal of Engineering Manufacture.* — Driven Right Leg circuit comparison.

---

## Known Limitations

This is an honest list of what this prototype cannot do (yet):

1. **Not real-time inner speech decoding.** This system detects silently *mouthed* commands — not pure thought. True "inner speech" with zero muscle activation is beyond current surface EMG technology.

2. **Session-dependent accuracy.** When you remove and re-place electrodes, accuracy drops 20-25% because electrode positions shift. Recalibration is needed each session.

3. **Limited vocabulary.** Practical accuracy maxes out at 5-10 distinct commands. Beyond that, confusion between similar words increases rapidly.

4. **Environmental sensitivity.** Fluorescent lights, nearby power cables, and other electronic devices add noise. Works best in quiet electrical environments.

5. **User training required.** Subjects improve with practice over 1-2 weeks. Initial accuracy may be discouraging.

6. **No continuous speech.** This is a command detector, not a speech recognizer. It classifies isolated words, not sentences.

7. **Motion artifacts.** Walking, turning your head, or touching the electrodes causes spurious signals that can trigger false commands.

8. **Individual variation.** Facial anatomy differs between people. Electrode positions that work for one person may not work for another. Always recalibrate.

9. **Prototype hardware.** Breadboard circuits have higher noise than PCB designs. Expect better performance if you move to a soldered PCB with proper grounding.

---

## Future Work

- [ ] **Custom PCB design** — Replace breadboard with a proper PCB for lower noise and smaller form factor
- [ ] **Dry electrodes** — Reusable gold-plated or stainless steel electrodes embedded in the chin strap
- [ ] **Transfer learning** — Reduce recalibration time using a pre-trained base model fine-tuned per session
- [ ] **Adaptive thresholding** — Auto-adjust to electrode drift during a session without manual recalibration
- [ ] **Bone conduction feedback** — Add a bone conduction speaker for closed-loop audio feedback (~$20-40)
- [ ] **MQTT integration** — Map commands to smart home actions via Home Assistant
- [ ] **ADS1299 upgrade** — 24-bit, 8-channel research-grade ADC for higher resolution and more electrode channels
- [ ] **Real-time CNN** — Replace SVM with a lightweight convolutional neural network for better accuracy on raw signals
- [ ] **Continuous word detection** — Detect command boundaries automatically instead of fixed-window classification
- [ ] **Cross-session model persistence** — Train a model that generalizes across electrode placements using domain adaptation

---

## License

This project is part of [Mindloft](https://github.com/qinnovates/mindloft) and is released under the [Apache License 2.0](../../LICENSE).

**Disclaimer:** This is experimental research hardware. The authors make no warranties about safety, accuracy, or fitness for any purpose. Use entirely at your own risk. See [Safety](#safety) for important warnings.
