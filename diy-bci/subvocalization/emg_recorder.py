#!/usr/bin/env python3
"""
EMG Subvocalization BCI — Python Companion
==========================================

Records training data from ESP32, trains classifier, runs real-time
command detection.

Usage:
    python emg_recorder.py test              # verify hardware
    python emg_recorder.py calibrate         # collect training data
    python emg_recorder.py train             # train classifier
    python emg_recorder.py live              # real-time detection
    python emg_recorder.py plot              # visualize signals
    python emg_recorder.py plot-training     # visualize training data

Requirements:
    pip install pyserial numpy scipy scikit-learn matplotlib joblib
"""

import sys
import os
import time
import csv
import argparse
from collections import deque, Counter
from pathlib import Path

import serial
import numpy as np
from scipy.signal import butter, filtfilt, iirnotch

# ============================================================
# CONFIGURATION
# ============================================================

# Serial port — adjust for your system
# macOS: /dev/tty.usbserial-XXXX or /dev/cu.usbserial-XXXX
# Linux: /dev/ttyUSB0
# Windows: COM3
SERIAL_PORT = "/dev/tty.usbserial-0001"
BAUD_RATE = 115200

# Signal processing
SAMPLE_RATE = 200       # Hz (must match firmware F setting)
NUM_CHANNELS = 4
HIGHPASS_FREQ = 20      # Hz
LOWPASS_FREQ = 100      # Hz (subvocal EMG is mostly 20-100 Hz)
NOTCH_FREQ = 60         # Hz (power line: 60 for US, 50 for EU)
FILTER_ORDER = 4

# Feature extraction
WINDOW_MS = 250         # ms per analysis window
WINDOW_OVERLAP = 0.5    # 50% overlap
WINDOW_SIZE = int(WINDOW_MS * SAMPLE_RATE / 1000)
STEP_SIZE = int(WINDOW_SIZE * (1 - WINDOW_OVERLAP))

# Classification
VOTE_COUNT = 5          # majority vote over N consecutive predictions
CONFIDENCE_THRESHOLD = 0.6  # minimum vote ratio to trigger command
SILENCE_LABEL = "silence"

# Training
DEFAULT_COMMANDS = ["yes", "no", "go", "stop", "select"]
REPS_PER_COMMAND = 25
RECORD_DURATION = 2.0   # seconds per trial
REST_DURATION = 2.0     # seconds between trials

# Paths
DATA_DIR = Path("emg_data")
MODEL_PATH = Path("subvocal_model.pkl")
SCALER_PATH = Path("subvocal_scaler.pkl")

# Channel names (for display)
CH_NAMES = ["Mentalis", "Masseter", "Submental", "Laryngeal"]


# ============================================================
# SERIAL COMMUNICATION
# ============================================================

class EMGDevice:
    """Manages serial connection to ESP32 EMG device."""

    def __init__(self, port=SERIAL_PORT, baud=BAUD_RATE):
        self.port = port
        self.baud = baud
        self.ser = None

    def connect(self):
        """Open serial connection."""
        print(f"Connecting to {self.port}...")
        self.ser = serial.Serial(self.port, self.baud, timeout=2)
        time.sleep(2.5)  # wait for ESP32 reset

        # Flush startup messages
        while self.ser.in_waiting:
            line = self.ser.readline().decode(errors="replace").strip()
            if line and not line.startswith("#"):
                break
            if line:
                print(f"  {line}")

        print("Connected.\n")

    def disconnect(self):
        """Close serial connection."""
        if self.ser and self.ser.is_open:
            self.send_command("X")  # stop streaming
            time.sleep(0.1)
            self.ser.close()

    def send_command(self, cmd):
        """Send a command string to the device."""
        self.ser.write(f"{cmd}\n".encode())
        time.sleep(0.05)

        # Read response lines (comments starting with #)
        responses = []
        while self.ser.in_waiting:
            line = self.ser.readline().decode(errors="replace").strip()
            if line.startswith("#"):
                responses.append(line)
                print(f"  {line}")
            elif line:
                break
        return responses

    def read_sample(self):
        """Read one CSV line and parse into (timestamp, channels).

        Returns None if line is a comment or unparseable.
        """
        if not self.ser or not self.ser.in_waiting:
            line = self.ser.readline().decode(errors="replace").strip()
        else:
            line = self.ser.readline().decode(errors="replace").strip()

        if not line or line.startswith("#"):
            return None

        parts = line.split(",")
        try:
            if len(parts) >= 5:
                timestamp = int(parts[0])
                channels = [int(parts[i + 1]) for i in range(NUM_CHANNELS)]
                label = parts[5] if len(parts) > 5 else None
                return timestamp, channels, label
        except (ValueError, IndexError):
            pass
        return None

    def stream_samples(self, duration_sec=None, max_samples=None):
        """Generator that yields (timestamp, channels) tuples.

        Stops after duration_sec or max_samples, whichever comes first.
        If neither specified, streams indefinitely.
        """
        self.send_command("S")
        start = time.time()
        count = 0

        try:
            while True:
                if duration_sec and (time.time() - start) >= duration_sec:
                    break
                if max_samples and count >= max_samples:
                    break

                result = self.read_sample()
                if result:
                    count += 1
                    yield result
        finally:
            self.send_command("X")

    def record_trial(self, duration_sec, label):
        """Record a single trial of fixed duration with label.

        Returns numpy array of shape (n_samples, 4).
        """
        samples = []
        self.send_command(f"L{label}")
        self.send_command("R")
        start = time.time()

        while time.time() - start < duration_sec:
            result = self.read_sample()
            if result:
                _, channels, _ = result
                samples.append(channels)

        self.send_command("X")
        return np.array(samples) if samples else np.empty((0, NUM_CHANNELS))


# ============================================================
# SIGNAL PROCESSING
# ============================================================

def bandpass_filter(signal, fs=SAMPLE_RATE, low=HIGHPASS_FREQ,
                    high=LOWPASS_FREQ, order=FILTER_ORDER):
    """Apply Butterworth bandpass filter."""
    nyq = fs / 2
    low_n = max(low / nyq, 0.001)
    high_n = min(high / nyq, 0.999)
    b, a = butter(order, [low_n, high_n], btype="bandpass")
    # Use filtfilt for zero-phase filtering (no lag)
    return filtfilt(b, a, signal, padlen=min(len(signal) - 1, 3 * order))


def notch_filter(signal, fs=SAMPLE_RATE, freq=NOTCH_FREQ, Q=30):
    """Apply IIR notch filter to remove power line interference."""
    b, a = iirnotch(freq, Q, fs)
    return filtfilt(b, a, signal, padlen=min(len(signal) - 1, 6))


def preprocess(signal, fs=SAMPLE_RATE):
    """Full preprocessing pipeline for one channel."""
    if len(signal) < 20:
        return signal
    signal = signal.astype(float)
    signal = notch_filter(signal, fs)
    signal = bandpass_filter(signal, fs)
    return signal


def preprocess_multichannel(data, fs=SAMPLE_RATE):
    """Preprocess all channels. data shape: (n_samples, n_channels)."""
    out = np.zeros_like(data, dtype=float)
    for ch in range(data.shape[1]):
        out[:, ch] = preprocess(data[:, ch], fs)
    return out


# ============================================================
# FEATURE EXTRACTION
# ============================================================

def extract_features(window):
    """Extract time-domain features from a 1D signal window.

    Returns list of 8 features.
    """
    N = len(window)
    if N == 0:
        return [0] * 8

    # Mean Absolute Value
    mav = np.mean(np.abs(window))

    # Root Mean Square
    rms = np.sqrt(np.mean(window ** 2))

    # Waveform Length (cumulative change)
    wl = np.sum(np.abs(np.diff(window)))

    # Variance
    var = np.var(window)

    # Integrated EMG
    iemg = np.sum(np.abs(window))

    # Zero Crossings (with threshold to reject noise)
    threshold = 0.01 * rms if rms > 0 else 0
    signs = np.sign(window)
    signs[np.abs(window) < threshold] = 0
    zc = np.sum(np.diff(signs) != 0)

    # Slope Sign Changes
    d = np.diff(window)
    ssc = np.sum(np.diff(np.sign(d)) != 0)

    # Average Amplitude Change
    aac = np.mean(np.abs(np.diff(window)))

    return [mav, rms, wl, var, iemg, zc, ssc, aac]


FEATURE_NAMES = ["MAV", "RMS", "WL", "VAR", "IEMG", "ZC", "SSC", "AAC"]


def extract_window_features(window_multichannel):
    """Extract features from all channels in a window.

    window_multichannel: shape (window_size, n_channels)
    Returns flat feature vector of length n_channels * 8.
    """
    features = []
    for ch in range(window_multichannel.shape[1]):
        features.extend(extract_features(window_multichannel[:, ch]))
    return features


def build_feature_matrix(data, labels_per_sample):
    """Build feature matrix from continuous multi-channel data.

    data: shape (n_samples, n_channels) — already preprocessed
    labels_per_sample: list of labels, one per sample

    Returns X (n_windows, n_features), y (n_windows,)
    """
    n_samples = data.shape[0]
    X, y = [], []

    for start in range(0, n_samples - WINDOW_SIZE, STEP_SIZE):
        end = start + WINDOW_SIZE
        window = data[start:end]

        # Use the label at the center of the window
        center = start + WINDOW_SIZE // 2
        label = labels_per_sample[center]

        features = extract_window_features(window)
        X.append(features)
        y.append(label)

    return np.array(X), np.array(y)


# ============================================================
# TRAINING DATA COLLECTION
# ============================================================

def collect_training_data(device, commands=None, reps=REPS_PER_COMMAND,
                          duration=RECORD_DURATION, rest=REST_DURATION):
    """Guided calibration session. Saves data to CSV files."""
    if commands is None:
        commands = DEFAULT_COMMANDS

    DATA_DIR.mkdir(exist_ok=True)
    timestamp_str = time.strftime("%Y%m%d_%H%M%S")

    print("=" * 50)
    print("  EMG SUBVOCALIZATION CALIBRATION")
    print("=" * 50)
    print(f"  Commands: {commands}")
    print(f"  Reps per command: {reps}")
    print(f"  Trial duration: {duration}s")
    print(f"  Rest between trials: {rest}s")
    print()
    input("  Press ENTER when electrodes are placed and ready... ")

    all_labels = [SILENCE_LABEL] + commands
    all_data = {label: [] for label in all_labels}

    for label in all_labels:
        print()
        print("-" * 50)
        if label == SILENCE_LABEL:
            print(f"  BASELINE: Relax jaw completely. No speaking.")
        else:
            print(f"  COMMAND: Silently mouth '{label}' when you see GO")
        print("-" * 50)
        input(f"  Press ENTER when ready for '{label}'... ")

        for i in range(reps):
            sys.stdout.write(f"  Trial {i + 1:2d}/{reps}: ")
            sys.stdout.flush()

            # Countdown
            for countdown in [3, 2, 1]:
                sys.stdout.write(f"{countdown}...")
                sys.stdout.flush()
                time.sleep(0.5)

            sys.stdout.write("GO! ")
            sys.stdout.flush()

            # Record
            trial_data = device.record_trial(duration, label)
            all_data[label].append(trial_data)

            n = len(trial_data)
            print(f"({n} samples)")

            # Rest
            if i < reps - 1:
                time.sleep(rest)

    # Save to CSV
    output_file = DATA_DIR / f"training_{timestamp_str}.csv"
    total_samples = 0

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ch1", "ch2", "ch3", "ch4", "label", "trial"])

        for label, trials in all_data.items():
            for trial_idx, trial in enumerate(trials):
                for sample in trial:
                    writer.writerow(list(sample) + [label, trial_idx])
                    total_samples += 1

    print()
    print("=" * 50)
    print(f"  CALIBRATION COMPLETE")
    print(f"  Saved: {output_file}")
    print(f"  Total samples: {total_samples}")
    print(f"  Labels: {list(all_data.keys())}")
    print("=" * 50)

    return output_file


# ============================================================
# MODEL TRAINING
# ============================================================

def train_model(data_file=None):
    """Train SVM classifier from recorded training data."""
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import (
        cross_val_score,
        StratifiedKFold,
    )
    from sklearn.metrics import classification_report, confusion_matrix
    import joblib

    # Find most recent training file if not specified
    if data_file is None:
        files = sorted(DATA_DIR.glob("training_*.csv"))
        if not files:
            print("No training data found. Run 'calibrate' first.")
            return
        data_file = files[-1]
        print(f"Using most recent: {data_file}")

    # Load data
    print(f"Loading {data_file}...")
    raw_data = []
    labels = []
    with open(data_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_data.append([
                int(row["ch1"]), int(row["ch2"]),
                int(row["ch3"]), int(row["ch4"]),
            ])
            labels.append(row["label"])

    data = np.array(raw_data, dtype=float)
    labels = np.array(labels)
    print(f"  Loaded {len(data)} samples, {len(np.unique(labels))} classes")

    # Preprocess
    print("Preprocessing...")
    data = preprocess_multichannel(data)

    # Extract features
    print("Extracting features...")
    X, y = build_feature_matrix(data, labels)
    print(f"  Feature matrix: {X.shape[0]} windows x {X.shape[1]} features")

    # Check class distribution
    unique, counts = np.unique(y, return_counts=True)
    print("  Class distribution:")
    for label, count in zip(unique, counts):
        print(f"    {label}: {count} windows")

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train SVM with cross-validation
    print("\nTraining SVM (RBF kernel)...")
    svm = SVC(kernel="rbf", C=10, gamma="scale", probability=True)

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(svm, X_scaled, y, cv=skf, scoring="accuracy")

    print(f"\n  Cross-validation accuracy: {scores.mean():.1%} "
          f"(+/- {scores.std():.1%})")
    print(f"  Per-fold: {', '.join(f'{s:.1%}' for s in scores)}")

    # Train final model on all data
    svm.fit(X_scaled, y)

    # Classification report
    y_pred = svm.predict(X_scaled)
    print(f"\nClassification report (on training data):")
    print(classification_report(y, y_pred))

    # Confusion matrix
    print("Confusion matrix:")
    cm = confusion_matrix(y, y_pred, labels=unique)
    # Header
    header = "          " + "  ".join(f"{l:>8}" for l in unique)
    print(header)
    for i, label in enumerate(unique):
        row = f"  {label:>8}" + "  ".join(f"{cm[i, j]:>8}" for j in range(len(unique)))
        print(row)

    # Save model and scaler
    joblib.dump(svm, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print(f"\nModel saved: {MODEL_PATH}")
    print(f"Scaler saved: {SCALER_PATH}")

    return svm, scaler


# ============================================================
# REAL-TIME CLASSIFICATION
# ============================================================

def run_live(device, callback=None):
    """Real-time subvocalization detection loop."""
    import joblib

    if not MODEL_PATH.exists():
        print("No trained model found. Run 'train' first.")
        return

    print("Loading model...")
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print(f"  Classes: {list(model.classes_)}")

    # Circular buffer for incoming samples
    buffer = deque(maxlen=WINDOW_SIZE)
    votes = deque(maxlen=VOTE_COUNT)
    last_command = None
    sample_count = 0

    print()
    print("=" * 50)
    print("  LIVE DETECTION — Listening for commands...")
    print("  Press Ctrl+C to stop")
    print("=" * 50)
    print()

    device.send_command(f"F{SAMPLE_RATE}")
    device.send_command("S")

    try:
        while True:
            result = device.read_sample()
            if result is None:
                continue

            _, channels, _ = result
            buffer.append(channels)
            sample_count += 1

            # Wait until buffer is full
            if len(buffer) < WINDOW_SIZE:
                if sample_count % 50 == 0:
                    sys.stdout.write(
                        f"\r  Filling buffer: {len(buffer)}/{WINDOW_SIZE}"
                    )
                    sys.stdout.flush()
                continue

            # Process every STEP_SIZE samples
            if sample_count % STEP_SIZE != 0:
                continue

            # Convert buffer to array and preprocess
            window = np.array(list(buffer), dtype=float)
            window = preprocess_multichannel(window)

            # Extract features
            features = extract_window_features(window)
            features = np.array(features).reshape(1, -1)
            features = scaler.transform(features)

            # Classify
            pred = model.predict(features)[0]
            proba = model.predict_proba(features).max()
            votes.append(pred)

            # Majority vote
            if len(votes) >= VOTE_COUNT:
                counter = Counter(votes)
                majority_label, majority_count = counter.most_common(1)[0]
                confidence = majority_count / len(votes)

                if (majority_label != SILENCE_LABEL
                        and confidence >= CONFIDENCE_THRESHOLD
                        and majority_label != last_command):
                    last_command = majority_label
                    print(f"\r  >> {majority_label.upper()}"
                          f"  (confidence: {confidence:.0%},"
                          f" probability: {proba:.2f})"
                          f"                    ")

                    if callback:
                        callback(majority_label, confidence)

                elif majority_label == SILENCE_LABEL:
                    last_command = None
                    sys.stdout.write(
                        f"\r  ... listening"
                        f"  (noise: {proba:.2f})"
                        f"                              "
                    )
                    sys.stdout.flush()

    except KeyboardInterrupt:
        print("\n\nStopped.")
    finally:
        device.send_command("X")


# ============================================================
# VISUALIZATION
# ============================================================

def plot_live(device, duration=10):
    """Live signal plot for verifying electrode placement."""
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, axes = plt.subplots(NUM_CHANNELS, 1, figsize=(12, 8),
                             sharex=True)
    fig.suptitle("EMG Channels — Live Signal", fontsize=14)

    display_samples = SAMPLE_RATE * 5  # 5 seconds visible
    data = np.zeros((display_samples, NUM_CHANNELS))
    lines = []

    for i, ax in enumerate(axes):
        line, = ax.plot([], [], linewidth=0.5)
        lines.append(line)
        ax.set_ylabel(CH_NAMES[i])
        ax.set_xlim(0, display_samples)
        ax.set_ylim(-2000, 2000)
        ax.grid(True, alpha=0.3)
    axes[-1].set_xlabel("Samples")

    device.send_command(f"F{SAMPLE_RATE}")
    device.send_command("S")

    sample_idx = [0]

    def update(frame):
        # Read available samples
        for _ in range(20):  # batch reads
            result = device.read_sample()
            if result:
                _, channels, _ = result
                idx = sample_idx[0] % display_samples
                data[idx] = channels
                sample_idx[0] += 1

        # Update lines
        for i, line in enumerate(lines):
            # Roll data so current position is at the right
            rolled = np.roll(data[:, i],
                             -(sample_idx[0] % display_samples))
            line.set_data(np.arange(display_samples), rolled)

        return lines

    ani = animation.FuncAnimation(fig, update, interval=50, blit=True)

    plt.tight_layout()
    try:
        plt.show()
    finally:
        device.send_command("X")


def plot_training_data(data_file=None):
    """Visualize recorded training data by label."""
    import matplotlib.pyplot as plt

    if data_file is None:
        files = sorted(DATA_DIR.glob("training_*.csv"))
        if not files:
            print("No training data found.")
            return
        data_file = files[-1]

    print(f"Plotting {data_file}...")

    # Load
    raw = {ch: [] for ch in range(NUM_CHANNELS)}
    labels = []
    with open(data_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for i, key in enumerate(["ch1", "ch2", "ch3", "ch4"]):
                raw[i].append(int(row[key]))
            labels.append(row["label"])

    unique_labels = sorted(set(labels))
    n_labels = len(unique_labels)

    fig, axes = plt.subplots(n_labels, NUM_CHANNELS,
                             figsize=(16, 3 * n_labels),
                             sharex=True, sharey=True)
    if n_labels == 1:
        axes = axes.reshape(1, -1)

    fig.suptitle("Training Data by Label and Channel", fontsize=14)

    for row, label in enumerate(unique_labels):
        indices = [i for i, l in enumerate(labels) if l == label]
        for col in range(NUM_CHANNELS):
            ax = axes[row, col]
            signal = np.array([raw[col][i] for i in indices])
            if len(signal) > 0:
                filtered = preprocess(signal)
                ax.plot(filtered, linewidth=0.3, alpha=0.8)
            if row == 0:
                ax.set_title(CH_NAMES[col])
            if col == 0:
                ax.set_ylabel(label)
            ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.show()


# ============================================================
# HARDWARE TEST
# ============================================================

def run_test(device):
    """Run self-test and verify hardware."""
    print("Running hardware self-test...\n")
    device.send_command("T")

    # Wait for test output
    time.sleep(3)
    while device.ser.in_waiting:
        line = device.ser.readline().decode(errors="replace").strip()
        print(f"  {line}")

    print()
    print("Quick signal check — clench your jaw for 3 seconds...")
    time.sleep(1)

    # Read a few samples to show signal is alive
    device.send_command(f"G3")  # PGA ±1.024V
    device.send_command("S")
    time.sleep(0.5)

    samples = []
    start = time.time()
    while time.time() - start < 3:
        result = device.read_sample()
        if result:
            _, channels, _ = result
            samples.append(channels)

    device.send_command("X")

    if samples:
        arr = np.array(samples)
        print(f"\n  Collected {len(arr)} samples in 3 seconds")
        print(f"  Effective rate: {len(arr) / 3:.0f} Hz")
        print()
        for i in range(NUM_CHANNELS):
            ch = arr[:, i]
            print(f"  CH{i + 1} ({CH_NAMES[i]:>10}): "
                  f"min={ch.min():6d}  max={ch.max():6d}  "
                  f"mean={ch.mean():8.1f}  std={ch.std():8.1f}")

        # Check for dead channels
        for i in range(NUM_CHANNELS):
            if arr[:, i].std() < 5:
                print(f"\n  WARNING: CH{i + 1} ({CH_NAMES[i]}) "
                      f"looks dead (std < 5). Check electrode contact.")
    else:
        print("  ERROR: No samples received. Check connection.")


# ============================================================
# COMMAND ACTIONS (map commands to system actions)
# ============================================================

def command_callback(command, confidence):
    """Called when a command is detected. Customize this."""
    # Example: map to keyboard shortcuts
    # Requires: pip install pyautogui
    # import pyautogui

    actions = {
        "yes":    lambda: print("    → Action: CONFIRM"),
        "no":     lambda: print("    → Action: CANCEL"),
        "go":     lambda: print("    → Action: NEXT"),
        "stop":   lambda: print("    → Action: PAUSE"),
        "select": lambda: print("    → Action: SELECT"),
    }

    action = actions.get(command)
    if action:
        action()

    # Example: keyboard simulation
    # key_map = {"yes": "enter", "no": "escape", "go": "right",
    #            "stop": "space", "select": "return"}
    # if command in key_map:
    #     pyautogui.press(key_map[command])

    # Example: MQTT for smart home
    # import paho.mqtt.publish as publish
    # publish.single(f"emg/command/{command}", "1",
    #                hostname="homeassistant.local")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="EMG Subvocalization BCI Companion",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  test           Run hardware self-test
  calibrate      Collect training data (guided)
  train          Train classifier from recorded data
  live           Real-time command detection
  plot           Live signal visualization
  plot-training  Visualize recorded training data

Example workflow:
  1. python emg_recorder.py test
  2. python emg_recorder.py calibrate
  3. python emg_recorder.py train
  4. python emg_recorder.py live
        """,
    )

    parser.add_argument("command",
                        choices=["test", "calibrate", "train",
                                 "live", "plot", "plot-training"],
                        help="Action to perform")
    parser.add_argument("--port", default=SERIAL_PORT,
                        help=f"Serial port (default: {SERIAL_PORT})")
    parser.add_argument("--commands", nargs="+", default=None,
                        help="Custom command words for calibration")
    parser.add_argument("--reps", type=int, default=REPS_PER_COMMAND,
                        help=f"Reps per command (default: {REPS_PER_COMMAND})")
    parser.add_argument("--data", type=str, default=None,
                        help="Specific training data file to use")

    args = parser.parse_args()

    # Commands that don't need device connection
    if args.command == "train":
        data_file = Path(args.data) if args.data else None
        train_model(data_file)
        return

    if args.command == "plot-training":
        data_file = Path(args.data) if args.data else None
        plot_training_data(data_file)
        return

    # Commands that need device connection
    device = EMGDevice(port=args.port)
    try:
        device.connect()

        if args.command == "test":
            run_test(device)

        elif args.command == "calibrate":
            collect_training_data(
                device,
                commands=args.commands,
                reps=args.reps,
            )

        elif args.command == "live":
            run_live(device, callback=command_callback)

        elif args.command == "plot":
            plot_live(device)

    except serial.SerialException as e:
        print(f"Serial error: {e}")
        print(f"Check that the device is connected and "
              f"port {args.port} is correct.")
        print("List ports: python -m serial.tools.list_ports")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterrupted.")

    finally:
        device.disconnect()


if __name__ == "__main__":
    main()
