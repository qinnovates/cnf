#!/usr/bin/env python3
"""
Export trained EMG model to TensorFlow.js format for in-browser inference.

Converts the scikit-learn SVM pipeline into a small Keras neural network
(MLP) that replicates its decision boundary, then exports to TFJS.

Alternatively, trains a fresh Keras model directly on the training data
for better TensorFlow.js compatibility.

Usage:
    # Option A: Convert existing sklearn model (distillation)
    python export_tfjs_model.py distill

    # Option B: Train a fresh Keras model from training data
    python export_tfjs_model.py train

    # Option C: Train from data + export in one step
    python export_tfjs_model.py train --data emg_data/training_20260204_103000.csv

Output:
    tfjs_model/
    ├── model.json          # TensorFlow.js model topology
    ├── group1-shard1of1.bin # Model weights (binary)
    ├── labels.json         # Class label mapping
    └── scaler.json         # Feature normalization parameters

Requirements:
    pip install tensorflow tensorflowjs scikit-learn numpy joblib
"""

import sys
import os
import json
import argparse
from pathlib import Path

import numpy as np

# ============================================================
# CONFIGURATION (must match emg_recorder.py)
# ============================================================
NUM_CHANNELS = 4
FEATURES_PER_CHANNEL = 8  # MAV, RMS, WL, VAR, IEMG, ZC, SSC, AAC
NUM_FEATURES = NUM_CHANNELS * FEATURES_PER_CHANNEL  # 32
SAMPLE_RATE = 200
HIGHPASS_FREQ = 20
LOWPASS_FREQ = 100
NOTCH_FREQ = 60
WINDOW_MS = 250
WINDOW_SIZE = int(WINDOW_MS * SAMPLE_RATE / 1000)  # 50
WINDOW_OVERLAP = 0.5
STEP_SIZE = int(WINDOW_SIZE * (1 - WINDOW_OVERLAP))

MODEL_PATH = Path("subvocal_model.pkl")
SCALER_PATH = Path("subvocal_scaler.pkl")
DATA_DIR = Path("emg_data")
OUTPUT_DIR = Path("tfjs_model")

FEATURE_NAMES = ["MAV", "RMS", "WL", "VAR", "IEMG", "ZC", "SSC", "AAC"]


# ============================================================
# FEATURE EXTRACTION (duplicated from emg_recorder.py)
# ============================================================
from scipy.signal import butter, filtfilt, iirnotch

def bandpass_filter(signal, fs=SAMPLE_RATE, low=HIGHPASS_FREQ,
                    high=LOWPASS_FREQ, order=4):
    nyq = fs / 2
    b, a = butter(order, [max(low/nyq, 0.001), min(high/nyq, 0.999)],
                  btype="bandpass")
    return filtfilt(b, a, signal, padlen=min(len(signal)-1, 12))

def notch_filter(signal, fs=SAMPLE_RATE, freq=NOTCH_FREQ, Q=30):
    b, a = iirnotch(freq, Q, fs)
    return filtfilt(b, a, signal, padlen=min(len(signal)-1, 6))

def preprocess(signal, fs=SAMPLE_RATE):
    if len(signal) < 20:
        return signal.astype(float)
    signal = signal.astype(float)
    signal = notch_filter(signal, fs)
    signal = bandpass_filter(signal, fs)
    return signal

def extract_features(window):
    N = len(window)
    if N == 0:
        return [0] * FEATURES_PER_CHANNEL
    mav = np.mean(np.abs(window))
    rms = np.sqrt(np.mean(window ** 2))
    wl = np.sum(np.abs(np.diff(window)))
    var = np.var(window)
    iemg = np.sum(np.abs(window))
    threshold = 0.01 * rms if rms > 0 else 0
    signs = np.sign(window)
    signs[np.abs(window) < threshold] = 0
    zc = np.sum(np.diff(signs) != 0)
    d = np.diff(window)
    ssc = np.sum(np.diff(np.sign(d)) != 0)
    aac = np.mean(np.abs(np.diff(window)))
    return [mav, rms, wl, var, iemg, zc, ssc, aac]

def extract_window_features(window_multichannel):
    features = []
    for ch in range(window_multichannel.shape[1]):
        features.extend(extract_features(window_multichannel[:, ch]))
    return features

def build_feature_matrix(data, labels):
    n_samples = data.shape[0]
    X, y = [], []
    for start in range(0, n_samples - WINDOW_SIZE, STEP_SIZE):
        end = start + WINDOW_SIZE
        window = data[start:end]
        center = start + WINDOW_SIZE // 2
        label = labels[center]
        features = extract_window_features(window)
        X.append(features)
        y.append(label)
    return np.array(X), np.array(y)

def load_training_data(data_file=None):
    import csv
    if data_file is None:
        files = sorted(DATA_DIR.glob("training_*.csv"))
        if not files:
            print("No training data found in emg_data/")
            sys.exit(1)
        data_file = files[-1]
    print(f"Loading {data_file}...")
    raw_data, labels = [], []
    with open(data_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_data.append([int(row["ch1"]), int(row["ch2"]),
                             int(row["ch3"]), int(row["ch4"])])
            labels.append(row["label"])
    data = np.array(raw_data, dtype=float)
    labels = np.array(labels)
    # Preprocess
    for ch in range(NUM_CHANNELS):
        data[:, ch] = preprocess(data[:, ch])
    X, y = build_feature_matrix(data, labels)
    return X, y


# ============================================================
# OPTION A: DISTILL SKLEARN MODEL INTO KERAS
# ============================================================
def distill_model():
    """Load sklearn SVM, generate soft labels, train Keras to match."""
    import joblib

    if not MODEL_PATH.exists() or not SCALER_PATH.exists():
        print(f"sklearn model not found at {MODEL_PATH}")
        print("Run 'python emg_recorder.py train' first, or use 'train' mode.")
        sys.exit(1)

    svm = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    class_labels = list(svm.classes_)
    n_classes = len(class_labels)

    print(f"Loaded SVM model with {n_classes} classes: {class_labels}")

    # Load training data to generate distillation targets
    X, y = load_training_data()
    X_scaled = scaler.transform(X)

    # Get soft probability targets from SVM
    soft_targets = svm.predict_proba(X_scaled)
    print(f"Feature matrix: {X_scaled.shape}")
    print(f"Soft targets: {soft_targets.shape}")

    # Build and train Keras model
    model, history = build_and_train_keras(
        X_scaled, soft_targets, y, class_labels, is_distillation=True)

    # Export
    export_tfjs(model, scaler, class_labels)


# ============================================================
# OPTION B: TRAIN KERAS DIRECTLY
# ============================================================
def train_keras(data_file=None):
    """Train a Keras MLP directly on training data."""
    from sklearn.preprocessing import StandardScaler, LabelEncoder

    X, y = load_training_data(data_file)

    # Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Encode labels
    class_labels = sorted(list(set(y)))
    n_classes = len(class_labels)
    label_map = {label: i for i, label in enumerate(class_labels)}
    y_int = np.array([label_map[label] for label in y])

    # One-hot encode
    y_onehot = np.zeros((len(y_int), n_classes))
    y_onehot[np.arange(len(y_int)), y_int] = 1.0

    print(f"Classes: {class_labels}")
    print(f"Feature matrix: {X_scaled.shape}")
    print(f"Class distribution:")
    for label in class_labels:
        count = np.sum(y == label)
        print(f"  {label}: {count} windows")

    # Build and train
    model, history = build_and_train_keras(
        X_scaled, y_onehot, y, class_labels, is_distillation=False)

    # Export
    export_tfjs(model, scaler, class_labels)


# ============================================================
# KERAS MODEL
# ============================================================
def build_and_train_keras(X, targets, y_str, class_labels,
                          is_distillation=False):
    """Build and train a small MLP for EMG classification."""
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    import tensorflow as tf
    from sklearn.model_selection import train_test_split

    n_features = X.shape[1]
    n_classes = len(class_labels)

    # Integer labels for metrics
    label_map = {label: i for i, label in enumerate(class_labels)}
    y_int = np.array([label_map[label] for label in y_str])

    # Train/val split
    X_train, X_val, t_train, t_val, yi_train, yi_val = train_test_split(
        X, targets, y_int, test_size=0.2, stratify=y_int, random_state=42)

    print(f"\nTrain: {len(X_train)}, Val: {len(X_val)}")

    # Model architecture — small MLP
    # Designed to run fast in the browser
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(n_features,)),
        tf.keras.layers.Dense(64, activation='relu',
                              kernel_regularizer=tf.keras.regularizers.l2(1e-4)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(32, activation='relu',
                              kernel_regularizer=tf.keras.regularizers.l2(1e-4)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(n_classes, activation='softmax')
    ])

    # Loss: KL divergence for distillation, categorical CE for direct training
    if is_distillation:
        loss = tf.keras.losses.KLDivergence()
    else:
        loss = tf.keras.losses.CategoricalCrossentropy()

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss=loss,
        metrics=['accuracy']
    )

    model.summary()

    # Callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss', patience=20, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss', factor=0.5, patience=8, min_lr=1e-6),
    ]

    # Train
    print("\nTraining...")
    history = model.fit(
        X_train, t_train,
        validation_data=(X_val, t_val),
        epochs=200,
        batch_size=32,
        callbacks=callbacks,
        verbose=1
    )

    # Evaluate
    val_pred = model.predict(X_val, verbose=0)
    val_pred_labels = np.argmax(val_pred, axis=1)
    val_accuracy = np.mean(val_pred_labels == yi_val)
    print(f"\nValidation accuracy: {val_accuracy:.1%}")

    # Per-class accuracy
    for i, label in enumerate(class_labels):
        mask = yi_val == i
        if mask.sum() > 0:
            class_acc = np.mean(val_pred_labels[mask] == i)
            print(f"  {label}: {class_acc:.1%} ({mask.sum()} samples)")

    return model, history


# ============================================================
# EXPORT TO TENSORFLOW.JS
# ============================================================
def export_tfjs(model, scaler, class_labels):
    """Export Keras model + scaler + labels to TFJS format."""
    import tensorflow as tf

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Save Keras model as SavedModel first
    saved_model_dir = OUTPUT_DIR / "saved_model"
    model.save(str(saved_model_dir))

    # Convert to TFJS
    try:
        import tensorflowjs as tfjs
        tfjs.converters.save_keras_model(model, str(OUTPUT_DIR))
        print(f"\nTFJS model saved to {OUTPUT_DIR}/model.json")
    except ImportError:
        print("\ntensorflowjs not installed. Converting via CLI:")
        print(f"  pip install tensorflowjs")
        print(f"  tensorflowjs_converter --input_format=tf_saved_model "
              f"--output_format=tfjs_graph_model "
              f"{saved_model_dir} {OUTPUT_DIR}")
        print("\nFalling back to manual weight export...")
        export_manual_weights(model, class_labels, scaler)
        return

    # Save class labels
    labels_path = OUTPUT_DIR / "labels.json"
    with open(labels_path, "w") as f:
        json.dump(class_labels, f)
    print(f"Labels saved to {labels_path}")

    # Save scaler parameters (mean, scale)
    scaler_path = OUTPUT_DIR / "scaler.json"
    scaler_data = {
        "mean": scaler.mean_.tolist(),
        "scale": scaler.scale_.tolist(),
        "n_features": int(scaler.n_features_in_)
    }
    with open(scaler_path, "w") as f:
        json.dump(scaler_data, f, indent=2)
    print(f"Scaler saved to {scaler_path}")

    # Save feature extraction config
    config_path = OUTPUT_DIR / "config.json"
    config = {
        "num_channels": NUM_CHANNELS,
        "features_per_channel": FEATURES_PER_CHANNEL,
        "feature_names": FEATURE_NAMES,
        "sample_rate": SAMPLE_RATE,
        "window_ms": WINDOW_MS,
        "window_size": WINDOW_SIZE,
        "window_overlap": WINDOW_OVERLAP,
        "highpass_freq": HIGHPASS_FREQ,
        "lowpass_freq": LOWPASS_FREQ,
        "notch_freq": NOTCH_FREQ,
        "class_labels": class_labels,
        "num_classes": len(class_labels),
    }
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {config_path}")

    # Print file sizes
    print(f"\nOutput files:")
    for p in sorted(OUTPUT_DIR.iterdir()):
        if p.is_file():
            size = p.stat().st_size
            if size > 1024:
                print(f"  {p.name}: {size/1024:.1f} KB")
            else:
                print(f"  {p.name}: {size} bytes")

    print(f"\nTo use in the web app:")
    print(f"  1. Serve {OUTPUT_DIR}/ via HTTP (or place alongside emg_ble_app.html)")
    print(f"  2. Open the web app and tap 'Load Model'")
    print(f"  3. Select the {OUTPUT_DIR}/ directory")


def export_manual_weights(model, class_labels, scaler):
    """Fallback: export weights as raw JSON for manual loading."""
    weights_data = {}
    for i, layer in enumerate(model.layers):
        w = layer.get_weights()
        if w:
            weights_data[f"layer_{i}_{layer.name}"] = {
                "type": layer.__class__.__name__,
                "weights": [arr.tolist() for arr in w]
            }

    weights_path = OUTPUT_DIR / "weights.json"
    with open(weights_path, "w") as f:
        json.dump(weights_data, f)
    print(f"Manual weights saved to {weights_path}")

    # Still save labels, scaler, config
    with open(OUTPUT_DIR / "labels.json", "w") as f:
        json.dump(class_labels, f)
    scaler_data = {
        "mean": scaler.mean_.tolist(),
        "scale": scaler.scale_.tolist(),
        "n_features": int(scaler.n_features_in_)
    }
    with open(OUTPUT_DIR / "scaler.json", "w") as f:
        json.dump(scaler_data, f, indent=2)


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(
        description="Export EMG classifier to TensorFlow.js")
    parser.add_argument("mode", choices=["distill", "train"],
        help="'distill' = convert sklearn SVM, 'train' = fresh Keras model")
    parser.add_argument("--data", type=str, default=None,
        help="Path to training CSV (default: most recent in emg_data/)")

    args = parser.parse_args()

    if args.mode == "distill":
        distill_model()
    elif args.mode == "train":
        train_keras(args.data)


if __name__ == "__main__":
    main()
