# ============================================================
# NumPy — Numerical Computing for AI
# Demonstrates: arrays, shapes, operations, statistics, reshaping.
# NumPy is the foundation of nearly every ML/AI library in Python.
# ============================================================

import numpy as np

print("NumPy for Machine Learning\n")

# ── 1. Creating a 1-D feature array ─────────────────────────
# Each value represents a measurement (e.g. sepal length, width for Iris dataset)
features = np.array([5.3, 3.5, 1.2, 0.4])
print(f"Features : {features}")
print(f"Shape    : {features.shape}")        # (4,) → 1-D array with 4 elements
print(f"Dtype    : {features.dtype}\n")      # float64 by default

# ── 2. Array arithmetic (element-wise) ──────────────────────
# Operations apply to every element — no loops needed!
scaled = features * 2                        # multiply each element by 2
print(f"Scaled (×2)     : {scaled}")

normalized = features / features.max()       # normalize to 0–1 range
print(f"Normalized (0-1): {normalized}\n")

# ── 3. Aggregate statistics ─────────────────────────────────
# Commonly used in data preprocessing before training ML models
print(f"Sum   : {features.sum():.2f}")
print(f"Mean  : {features.mean():.2f}")
print(f"Std   : {features.std():.2f}")
print(f"Min   : {features.min():.2f}")
print(f"Max   : {features.max():.2f}\n")

# ── 4. Reshaping — 1-D to 2-D ──────────────────────────────
# ML models usually expect 2-D input: (samples, features)
reshaped = features.reshape(1, -1)           # -1 means "infer this dimension"
print(f"Reshaped (1×4)  : {reshaped}")
print(f"Shape           : {reshaped.shape}\n")

# ── 5. Creating common arrays ───────────────────────────────
zeros = np.zeros(5)                          # [0. 0. 0. 0. 0.]
ones  = np.ones(5)                           # [1. 1. 1. 1. 1.]
rng   = np.arange(0, 10, 2)                  # [0, 2, 4, 6, 8]

print(f"Zeros  : {zeros}")
print(f"Ones   : {ones}")
print(f"Range  : {rng}")