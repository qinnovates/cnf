# BCI Proof-of-Concept Build Guide

> A step-by-step guide to building a low-cost BCI development kit for testing
> NSP protocol concepts, QIF signal analysis, and Runemate Forge rendering.
>
> **Status:** Draft
> **Version:** 0.1 (2026-02-07)
> **Author:** Kevin Qi
> **Budget:** ~$500-1,200 depending on EEG hardware choice

---

## 1. Overview

This guide covers building a three-phase BCI proof-of-concept:

| Phase | Goal | Hardware | Software |
|-------|------|----------|----------|
| **Phase 0** | Signal acquisition + visualization | EEG board + laptop | BrainFlow + Python |
| **Phase 1** | Edge processing + haptic feedback | + Raspberry Pi + bone conduction | + NSP reference encoder |
| **Phase 2** | PQ-encrypted pipeline | Same hardware | + liboqs + Runemate decoder |

Each phase builds on the previous. You can stop at any phase and have a working demo.

---

## 2. Bill of Materials

### Phase 0: Signal Acquisition (~$250-1,000)

| Component | Option A (Budget) | Option B (Research-grade) |
|-----------|-------------------|--------------------------|
| **EEG Board** | Muse 2 (~$250) | OpenBCI Cyton 8-ch (~$500) |
| **Electrodes** | Built into Muse headband | Gold cup electrodes + Ten20 paste (~$50) |
| **Headset** | Built-in | OpenBCI Ultracortex Mark IV (~$350) or DIY 3D print |
| **Computer** | Any laptop with Bluetooth | Any laptop with USB (dongle) |
| **Software** | BrainFlow (free, open-source) | BrainFlow (free, open-source) |
| **Subtotal** | **~$250** | **~$900** |

**Which to choose:**
- **Muse 2**: 4 channels (AF7, AF8, TP9, TP10), 256 Hz, Bluetooth. Great for quick demos, emotion/meditation, and "does this work?" validation. Limited channel count means no motor imagery BCI.
- **OpenBCI Cyton**: 8 channels (expandable to 16 with Daisy), 250 Hz, WiFi/BLE via dongle. Research-grade. Supports motor imagery, P300, SSVEP paradigms. This is what you want for serious NSP testing.

> **Recommendation:** Start with Muse 2 for immediate demos. Upgrade to OpenBCI Cyton when you need multi-channel motor imagery or P300 paradigms.

### Phase 1: Edge Processing + Haptic Feedback (~$80-120)

| Component | Model | Price | Notes |
|-----------|-------|-------|-------|
| **Single-board computer** | Raspberry Pi Zero 2W | ~$15-20 | Quad-core ARM Cortex-A53, 512 MB RAM, WiFi/BLE |
| **MicroSD card** | 32 GB Class 10 | ~$8 | For Raspberry Pi OS |
| **Power** | USB-C power bank (10,000 mAh) | ~$15 | Or USB-C wall adapter |
| **Bone conduction transducer** | Dayton Audio DAEX25FHE-4 | ~$12 | 25mm exciter, 4 ohm, 20W max |
| **Audio amplifier** | Adafruit I2S 3W Class D (MAX98357A) | ~$6 | I2S input from Pi, drives bone conduction |
| **Misc** | Jumper wires, breadboard, header pins | ~$10 | Standard prototyping kit |
| **Case** | Pi Zero case (optional) | ~$5 | Or 3D print |
| **Subtotal** | | **~$70-80** |

**Alternative bone conduction options:**
- Dayton Audio DAEX19-4 (19mm, lighter, lower power) — ~$8
- Dayton Audio DAEX32EP-4 (32mm, more bass) — ~$15
- Any small piezo disc transducer — ~$2-5 (lower quality but functional for PoC)

### Phase 2: PQ-Encrypted Pipeline (~$0 additional)

No new hardware needed. Phase 2 is purely software:
- liboqs (Open Quantum Safe) — free, open-source PQ crypto library
- Runemate Forge decoder — our Staves bytecode interpreter
- NSP reference implementation — Python encoder/decoder

### Total BOM

| Configuration | Total Cost |
|---------------|-----------|
| **Minimum** (Muse 2 + Pi Zero + bone conduction) | **~$330** |
| **Recommended** (OpenBCI Cyton + Pi Zero + bone conduction) | **~$980** |
| **Full** (OpenBCI Cyton + Ultracortex + Pi Zero + bone conduction) | **~$1,200** |

---

## 3. Phase 0: Signal Acquisition

### 3.1 Install BrainFlow

BrainFlow is a universal API that works with OpenBCI, Muse, Emotiv, NeuroSky, and 20+ other boards.

```bash
# Python 3.9+
pip install brainflow numpy matplotlib
```

### 3.2 Connect Your EEG Board

**Muse 2 (Bluetooth):**
```python
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

params = BrainFlowInputParams()
# Muse 2 uses Bluetooth — no serial port needed
board = BoardShim(BoardIds.MUSE_2_BOARD, params)
board.prepare_session()
board.start_stream()
```

**OpenBCI Cyton (USB Dongle):**
```python
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

params = BrainFlowInputParams()
params.serial_port = "/dev/tty.usbserial-XXXX"  # Find with: ls /dev/tty.usb*
board = BoardShim(BoardIds.CYTON_BOARD, params)
board.prepare_session()
board.start_stream()
```

### 3.3 Visualize Live EEG

```python
import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes

# Setup (use your board ID)
params = BrainFlowInputParams()
board = BoardShim(BoardIds.MUSE_2_BOARD, params)
board.prepare_session()
board.start_stream()

# Get channel info
eeg_channels = BoardShim.get_eeg_channels(BoardIds.MUSE_2_BOARD)
sampling_rate = BoardShim.get_sampling_rate(BoardIds.MUSE_2_BOARD)
print(f"EEG channels: {eeg_channels}, Sampling rate: {sampling_rate} Hz")

# Collect 5 seconds of data
time.sleep(5)
data = board.get_board_data()
board.stop_stream()
board.release_session()

# Extract EEG and filter
for ch in eeg_channels:
    DataFilter.perform_bandpass(data[ch], sampling_rate, 1.0, 50.0, 4,
                                FilterTypes.BUTTERWORTH, 0)

# Basic power spectrum
for ch in eeg_channels:
    psd = DataFilter.get_psd_welch(data[ch], 256, 128, sampling_rate,
                                    WindowOperations.HAMMING)
    print(f"Channel {ch}: Delta={np.mean(psd[0][1:4]):.2f}, "
          f"Theta={np.mean(psd[0][4:8]):.2f}, "
          f"Alpha={np.mean(psd[0][8:13]):.2f}, "
          f"Beta={np.mean(psd[0][13:30]):.2f}")
```

### 3.4 What You Should See

| Band | Frequency | Expected Activity |
|------|-----------|-------------------|
| Delta | 1-4 Hz | Low (unless drowsy) |
| Theta | 4-8 Hz | Moderate (relaxed focus) |
| Alpha | 8-13 Hz | **High with eyes closed**, drops with eyes open |
| Beta | 13-30 Hz | Active thinking, motor preparation |
| Gamma | 30-50 Hz | High-level processing (often noisy in consumer EEG) |

**Quick validation test:** Close your eyes for 10 seconds, then open them. You should see alpha power (8-13 Hz) spike during eyes-closed and drop when you open them. If you see this, your EEG is working correctly.

### 3.5 Phase 0 Deliverables

- [ ] Live EEG data streaming to laptop
- [ ] Band power visualization (delta, theta, alpha, beta)
- [ ] Alpha eyes-open/eyes-closed validation
- [ ] Data saved to CSV for offline analysis

---

## 4. Phase 1: Edge Processing + Haptic Feedback

### 4.1 Set Up Raspberry Pi Zero 2W

```bash
# Flash Raspberry Pi OS Lite (64-bit) to MicroSD card
# Use Raspberry Pi Imager: https://www.raspberrypi.com/software/

# On first boot, enable SSH and WiFi via raspi-config
sudo raspi-config
# Interface Options → SSH → Enable
# System Options → Wireless LAN → Enter WiFi credentials

# Update and install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git libasound2-dev

# Create project environment
python3 -m venv ~/bci-poc
source ~/bci-poc/bin/activate
pip install brainflow numpy
```

### 4.2 Wire Bone Conduction Transducer

The Dayton Audio DAEX25FHE-4 is a surface exciter that turns any surface (or your skull) into a speaker via vibration.

```
Raspberry Pi Zero 2W          MAX98357A I2S Amp         DAEX25FHE-4
┌──────────────┐              ┌──────────────┐          ┌──────────┐
│ GPIO 18 (CLK)├──────────────┤ BCLK         │          │          │
│ GPIO 19 (FS) ├──────────────┤ LRC          │          │ Speaker  │
│ GPIO 21 (DO) ├──────────────┤ DIN          │   +/- ──►│ Leads    │
│ 5V           ├──────────────┤ VIN          │          │          │
│ GND          ├──────────────┤ GND          │          └──────────┘
└──────────────┘              │ + ───────────┼──────────► + (red)
                              │ - ───────────┼──────────► - (black)
                              └──────────────┘
```

**Enable I2S on the Pi:**
```bash
# Add to /boot/config.txt:
dtoverlay=hifiberry-dac

# Reboot
sudo reboot
```

**Test audio output:**
```bash
# Generate a test tone
speaker-test -t sine -f 440 -l 1
# You should feel vibration through the bone conduction transducer
```

### 4.3 Real-Time EEG → Haptic Feedback Loop

This script streams EEG from the board, computes band power on the Pi, and drives the bone conduction transducer with a frequency mapped to brain state.

```python
#!/usr/bin/env python3
"""
BCI PoC Phase 1: EEG → Edge Processing → Bone Conduction Feedback
Streams EEG data, computes band power, maps to haptic vibration.
"""

import time
import numpy as np
import subprocess
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes

# Configuration
BOARD_ID = BoardIds.MUSE_2_BOARD  # Change for your board
SAMPLE_RATE = 256
WINDOW_SEC = 1  # 1-second analysis windows
FEEDBACK_INTERVAL = 0.5  # Update haptic every 500ms

def compute_band_power(data, channel, sample_rate):
    """Compute power in standard EEG bands."""
    DataFilter.perform_bandpass(data[channel], sample_rate, 1.0, 50.0, 4,
                                FilterTypes.BUTTERWORTH, 0)
    psd = DataFilter.get_psd_welch(data[channel], 256, 128, sample_rate,
                                    WindowOperations.HAMMING)
    freqs = psd[1]
    powers = psd[0]

    bands = {
        'delta': np.mean(powers[(freqs >= 1) & (freqs < 4)]),
        'theta': np.mean(powers[(freqs >= 4) & (freqs < 8)]),
        'alpha': np.mean(powers[(freqs >= 8) & (freqs < 13)]),
        'beta':  np.mean(powers[(freqs >= 13) & (freqs < 30)]),
    }
    return bands

def map_to_haptic(bands):
    """Map brain state to bone conduction frequency and intensity."""
    # High alpha = relaxed → low frequency hum
    # High beta = focused → higher frequency pulse
    # High theta = drowsy → warning pulse
    alpha_ratio = bands['alpha'] / (bands['beta'] + 1e-6)

    if alpha_ratio > 2.0:
        return 80, 0.3   # Relaxed: low hum
    elif alpha_ratio < 0.5:
        return 200, 0.6  # Focused: medium buzz
    else:
        return 120, 0.4  # Neutral: gentle pulse

def play_tone(freq, duration=0.3, volume=0.5):
    """Play a tone through the bone conduction transducer."""
    # Using sox (install: sudo apt install sox)
    subprocess.Popen(
        ['play', '-n', 'synth', str(duration), 'sine', str(freq),
         'vol', str(volume)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

def main():
    params = BrainFlowInputParams()
    board = BoardShim(BOARD_ID, params)
    eeg_channels = BoardShim.get_eeg_channels(BOARD_ID)

    board.prepare_session()
    board.start_stream()
    print("Streaming... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(FEEDBACK_INTERVAL)
            data = board.get_current_board_data(SAMPLE_RATE * WINDOW_SEC)

            if data.shape[1] < SAMPLE_RATE:
                continue

            # Compute band power (average across channels)
            all_bands = []
            for ch in eeg_channels:
                all_bands.append(compute_band_power(data, ch, SAMPLE_RATE))

            avg_bands = {
                k: np.mean([b[k] for b in all_bands])
                for k in all_bands[0].keys()
            }

            freq, vol = map_to_haptic(avg_bands)
            play_tone(freq, duration=0.2, volume=vol)

            print(f"Alpha: {avg_bands['alpha']:.1f}  "
                  f"Beta: {avg_bands['beta']:.1f}  "
                  f"→ Haptic: {freq} Hz @ {vol:.1f}")

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        board.stop_stream()
        board.release_session()

if __name__ == "__main__":
    main()
```

### 4.4 Phase 1 Deliverables

- [ ] Pi Zero 2W running headless with SSH access
- [ ] BrainFlow streaming EEG data to Pi via BLE/WiFi
- [ ] Real-time band power computation on Pi
- [ ] Bone conduction transducer responding to brain state
- [ ] Latency measurement: EEG event → haptic response (target: <200ms)

---

## 5. Phase 2: PQ-Encrypted Pipeline

### 5.1 Install Post-Quantum Crypto

```bash
# Install liboqs (Open Quantum Safe)
pip install oqs

# Or build from source for ARM:
git clone https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
pip install .
```

### 5.2 NSP Frame Encoder (Simplified)

```python
#!/usr/bin/env python3
"""
NSP Frame Encoder - Simplified PoC
Demonstrates: Compress → Encrypt (AES-256-GCM) → Sign (ML-DSA)
"""

import struct
import hashlib
import os
import time
import oqs
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# NSP Frame Format (simplified)
NSP_MAGIC = b"NSP\x01"
NSP_VERSION = 1

def compress_eeg(raw_data: np.ndarray) -> bytes:
    """Delta encode EEG data for compression."""
    # Delta encoding: store first sample, then differences
    compressed = struct.pack('<f', raw_data[0])
    deltas = np.diff(raw_data).astype(np.int16)
    compressed += deltas.tobytes()
    return compressed

def build_nsp_frame(eeg_data: np.ndarray, qi_score: float,
                    band_id: int, seq_num: int) -> bytes:
    """Build an NSP frame: header + compressed payload."""
    payload = compress_eeg(eeg_data)
    timestamp = int(time.time() * 1000)  # ms precision

    header = NSP_MAGIC
    header += struct.pack('<BHQfBH',
        NSP_VERSION,
        len(payload),
        timestamp,
        qi_score,
        band_id,
        seq_num
    )

    return header + payload

def encrypt_frame(frame: bytes, session_key: bytes) -> tuple[bytes, bytes]:
    """AES-256-GCM authenticated encryption."""
    nonce = os.urandom(12)
    aesgcm = AESGCM(session_key)
    ciphertext = aesgcm.encrypt(nonce, frame, None)
    return nonce, ciphertext

def pq_key_exchange():
    """ML-KEM-768 key encapsulation (post-quantum key exchange)."""
    kem = oqs.KeyEncapsulation("ML-KEM-768")

    # Server generates keypair
    server_pk = kem.generate_keypair()

    # Client encapsulates (creates shared secret)
    ciphertext, shared_secret_client = kem.encap_secret(server_pk)

    # Server decapsulates (recovers shared secret)
    shared_secret_server = kem.decap_secret(ciphertext)

    assert shared_secret_client == shared_secret_server
    print(f"ML-KEM-768 key exchange successful")
    print(f"  Public key:     {len(server_pk):,} bytes")
    print(f"  Ciphertext:     {len(ciphertext):,} bytes")
    print(f"  Shared secret:  {len(shared_secret_client)} bytes")

    # Derive AES-256 session key from shared secret
    session_key = hashlib.sha256(shared_secret_client).digest()
    return session_key

def pq_sign_frame(frame: bytes):
    """ML-DSA-65 digital signature (post-quantum authentication)."""
    sig = oqs.Signature("ML-DSA-65")
    signer_pk = sig.generate_keypair()

    signature = sig.sign(frame)

    is_valid = sig.verify(frame, signature, signer_pk)
    print(f"ML-DSA-65 signature")
    print(f"  Public key:  {len(signer_pk):,} bytes")
    print(f"  Signature:   {len(signature):,} bytes")
    print(f"  Valid:        {is_valid}")

    return signature, signer_pk
```

### 5.3 Runemate Staves Decoder (On-Pi)

For Phase 2, the Pi also runs a lightweight Staves bytecode interpreter to render BCI dashboard content received over the PQ-encrypted channel.

```python
#!/usr/bin/env python3
"""
Runemate Scribe - Staves Bytecode Interpreter (PoC)
Decodes .stav files and extracts semantic content for display.
"""

import struct

STAVES_MAGIC = b"STAV"
OP_OPEN = 0x01
OP_CLOSE = 0x02
OP_TEXT = 0x03
OP_ATTR = 0x04
OP_STYLE_REF = 0x05
OP_EOF = 0xFF

TAG_NAMES = {
    0x01: "html", 0x02: "head", 0x03: "body", 0x04: "div", 0x05: "span",
    0x06: "p", 0x07: "h1", 0x08: "h2", 0x09: "h3", 0x0A: "h4",
    0x0B: "a", 0x0C: "img", 0x0D: "button", 0x0E: "input", 0x0F: "form",
    0x10: "table", 0x11: "tr", 0x12: "td", 0x13: "th",
}

def decode_staves(binary: bytes):
    """Decode a Staves binary and print its semantic content."""
    if binary[:4] != STAVES_MAGIC:
        raise ValueError("Not a valid Staves binary")

    version = struct.unpack_from('<H', binary, 4)[0]
    sp_offset = struct.unpack_from('<I', binary, 8)[0]
    st_offset = struct.unpack_from('<I', binary, 12)[0]

    # Read string pool
    strings = []
    pos = sp_offset
    count = struct.unpack_from('<H', binary, pos)[0]
    pos += 2
    for _ in range(count):
        slen = struct.unpack_from('<H', binary, pos)[0]
        pos += 2
        strings.append(binary[pos:pos+slen].decode('utf-8'))
        pos += slen

    # Skip style table, find DOM opcodes
    st_count = struct.unpack_from('<H', binary, st_offset)[0]
    pos = st_offset + 2
    for _ in range(st_count):
        prop_count = struct.unpack_from('<B', binary, pos)[0]
        pos += 1 + prop_count * 3  # Each prop: 1 byte ID + 2 byte value_idx

    # Decode DOM opcodes
    depth = 0
    while pos < len(binary):
        op = binary[pos]
        pos += 1

        if op == OP_EOF:
            break
        elif op == OP_OPEN:
            tag_id = binary[pos]
            attr_count = binary[pos+1]
            pos += 2
            tag_name = TAG_NAMES.get(tag_id, f"tag_{tag_id:#x}")
            if tag_id == 0x00:
                idx = struct.unpack_from('<H', binary, pos)[0]
                tag_name = strings[idx] if idx < len(strings) else "unknown"
                pos += 2
            print("  " * depth + f"<{tag_name}>")
            depth += 1
        elif op == OP_CLOSE:
            depth = max(0, depth - 1)
        elif op == OP_TEXT:
            idx = struct.unpack_from('<H', binary, pos)[0]
            pos += 2
            text = strings[idx] if idx < len(strings) else ""
            if text:
                print("  " * depth + text)
        elif op == OP_ATTR:
            pos += 4  # name_idx + value_idx
        elif op == OP_STYLE_REF:
            pos += 2  # style_idx

    print(f"\nDecoded: {len(strings)} strings, {st_count} styles")
```

### 5.4 Full Pipeline Demo

```python
#!/usr/bin/env python3
"""
Full NSP + Runemate Pipeline Demo

Demonstrates the complete data flow:
1. Acquire EEG via BrainFlow
2. Compress + build NSP frame
3. PQ key exchange (ML-KEM-768)
4. Encrypt frame (AES-256-GCM)
5. Sign frame (ML-DSA-65)
6. Transmit (simulated)
7. Verify + decrypt + decompress on receiver
8. Decode Staves content for display
"""

# Import all modules from above, then:

def demo_pipeline():
    print("=" * 60)
    print("  NSP + RUNEMATE FORGE: FULL PIPELINE DEMO")
    print("=" * 60)

    # Step 1: Simulate EEG data (or use real board)
    print("\n[1] Generating synthetic EEG data...")
    eeg_data = np.random.randn(256).astype(np.float32) * 50  # 1 sec @ 256 Hz

    # Step 2: Build NSP frame
    print("[2] Building NSP frame (compress + header)...")
    frame = build_nsp_frame(eeg_data, qi_score=0.85, band_id=3, seq_num=1)
    print(f"    Raw EEG: {len(eeg_data) * 4:,} bytes")
    print(f"    NSP frame: {len(frame):,} bytes")

    # Step 3: PQ key exchange
    print("\n[3] Post-quantum key exchange (ML-KEM-768)...")
    session_key = pq_key_exchange()

    # Step 4: Encrypt
    print("\n[4] Encrypting frame (AES-256-GCM)...")
    nonce, ciphertext = encrypt_frame(frame, session_key)
    print(f"    Ciphertext: {len(ciphertext):,} bytes (+{len(ciphertext)-len(frame)} auth tag)")

    # Step 5: Sign
    print("\n[5] Signing frame (ML-DSA-65)...")
    signature, signer_pk = pq_sign_frame(ciphertext)

    # Step 6: Total transmission size
    total = len(nonce) + len(ciphertext) + len(signature)
    print(f"\n[6] Total transmission: {total:,} bytes")
    print(f"    Nonce:      {len(nonce)} bytes")
    print(f"    Ciphertext: {len(ciphertext):,} bytes")
    print(f"    Signature:  {len(signature):,} bytes")

    # Step 7: Load and decode a Staves binary
    print("\n[7] Decoding Staves content...")
    stav_path = "runemate-poc/output/bci-alert.stav"
    try:
        with open(stav_path, 'rb') as f:
            staves_binary = f.read()
        print(f"    Loaded {stav_path}: {len(staves_binary)} bytes")
        decode_staves(staves_binary)
    except FileNotFoundError:
        print(f"    {stav_path} not found — run staves_compiler.py first")

    print("\n" + "=" * 60)
    print("  PIPELINE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    demo_pipeline()
```

### 5.5 Phase 2 Deliverables

- [ ] ML-KEM-768 key exchange working on Pi Zero 2W
- [ ] AES-256-GCM encryption of NSP frames
- [ ] ML-DSA-65 signature generation and verification
- [ ] Staves bytecode decoder running on Pi
- [ ] End-to-end latency: EEG → compress → encrypt → sign → decrypt → verify (target: <500ms for PoC)
- [ ] Bandwidth measurement: total bytes/sec with PQ overhead

---

## 6. Safety

### Electrical Safety (CRITICAL)

| Rule | Why |
|------|-----|
| **Never connect mains power to electrodes** | Fatal. Always use battery-powered devices or USB isolation. |
| **Never exceed 50 μA DC through scalp electrodes** | IEC 60601-1 medical device limit. Consumer EEG boards enforce this in hardware. |
| **Use only medical-grade electrode gel/paste** | Ten20, Signa Gel, or similar. Never use random conductive materials. |
| **Never modify electrode hardware** | Consumer boards (Muse, OpenBCI) are designed with current-limiting circuits. Don't bypass them. |
| **Check impedance before recording** | High impedance = bad contact = noise. OpenBCI software shows impedance per channel. Target <10 kΩ. |
| **Clean electrode sites with alcohol wipe** | Reduces impedance, improves signal, prevents skin irritation. |

### Software Safety

| Rule | Why |
|------|-----|
| **This is READ-ONLY** | We are reading EEG signals, not stimulating. The PoC has no stimulation capability. |
| **No closed-loop stimulation** | The bone conduction feedback is haptic/audio only, not neural stimulation. |
| **Log everything** | Record all data for later analysis. Timestamp every frame. |

### What This PoC is NOT

- **Not a medical device.** Do not use for diagnosis or treatment.
- **Not FDA-approved.** This is a research/education tool.
- **Not implantable.** All components are external, non-invasive.
- **Not a brain stimulator.** We read signals. We do not write them.

---

## 7. Demo Scenarios

### Demo 1: "Alpha Detection" (Phase 0, 2 minutes)

1. Start EEG streaming
2. Subject closes eyes → alpha power increases
3. Subject opens eyes → alpha power drops
4. Show live power spectrum plot

**Pitch line:** "This is the signal. Now imagine this going through quantum-vulnerable Bluetooth."

### Demo 2: "Brain-to-Bone" (Phase 1, 5 minutes)

1. Start EEG + haptic feedback loop
2. Subject relaxes → low-frequency hum through bone conduction
3. Subject focuses (mental math) → higher-frequency buzz
4. Show real-time state classification

**Pitch line:** "Your brain state is being read, processed on edge hardware, and fed back through your skull — all in under 200 milliseconds."

### Demo 3: "PQ-Encrypted Neural Data" (Phase 2, 5 minutes)

1. Run full pipeline demo
2. Show ML-KEM key exchange sizes (1,184 bytes vs 32 bytes classical)
3. Show encrypted NSP frame (indistinguishable from noise)
4. Show Staves bytecode rendering (compressed dashboard)
5. Compare: Classical+HTML vs PQ+Staves total transmission

**Pitch line:** "Post-quantum security adds 3.5x to the handshake. Runemate compression saves 80%. Net result: more secure AND more efficient."

---

## 8. Troubleshooting

| Problem | Solution |
|---------|----------|
| Muse 2 won't connect via BrainFlow | Ensure Bluetooth is on. Try `BoardIds.MUSE_2_BLED_BOARD` (BLE Direct) instead. |
| OpenBCI no serial port found | Check USB dongle is plugged in. Run `ls /dev/tty.usb*` to find port. |
| Pi Zero 2W can't stream 250 Hz | Reduce to 4 channels or lower sample rate. Pi Zero has limited CPU. |
| Bone conduction no sound | Check I2S overlay in `/boot/config.txt`. Test with `speaker-test`. |
| liboqs import error on ARM | Build liboqs from source with `-DOQS_USE_OPENSSL=OFF` for ARM compatibility. |
| High noise in EEG | Check electrode impedance. Move away from power outlets (60 Hz noise). Use notch filter. |

---

## References

- [BrainFlow Documentation](https://brainflow.readthedocs.io/)
- [OpenBCI Getting Started](https://docs.openbci.com/)
- [Muse 2 Specifications](https://choosemuse.com/)
- [Open Quantum Safe (liboqs)](https://openquantumsafe.org/)
- [Raspberry Pi Zero 2W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
- [Dayton Audio DAEX25FHE-4](https://www.daytonaudio.com/product/1270/daex25fhe-4-framed-high-efficiency-25mm-exciter)
- [Adafruit MAX98357A I2S Amp](https://www.adafruit.com/product/3006)
- NSP Protocol Specification: see NSP-PROTOCOL-SPEC.md
- Runemate Forge: see RUNEMATE.md

---

*Part of the QIF (Quantum Indeterministic Framework) ecosystem.*
*"Read the brain. Protect the signal. Prove the math."*
