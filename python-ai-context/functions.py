# ============================================================
# Data Normalization Functions for ML Models
# Demonstrates: min-max scaling and z-score normalization.
# These are essential preprocessing steps before training
# any machine learning model.
# ============================================================


def normalize_data(data, method='min-max'):
    """
    Normalize a list of numerical values.

    Args:
        data   (list): Raw numerical data to normalize.
        method (str):  Normalization method — 'min-max' or 'z-score'.

    Returns:
        list: Normalized values.

    Raises:
        ValueError: If an unknown method is provided.
    """

    if method == 'min-max':
        # ── Min-Max Scaling ──────────────────────────────
        # Rescales values to [0, 1] range
        # Formula: (x - min) / (max - min)
        min_val = min(data)
        max_val = max(data)
        return [(x - min_val) / (max_val - min_val) for x in data]

    elif method == 'z-score':
        # ── Z-Score Normalization ────────────────────────
        # Centers data around 0 with unit standard deviation
        # Formula: (x - mean) / std
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std = variance ** 0.5
        return [(x - mean) / std for x in data]

    else:
        raise ValueError(f"Unknown method '{method}'. Use 'min-max' or 'z-score'.")


# ── Demo ─────────────────────────────────────────────────────
raw_data = [10, 20, 30, 40, 50]

# Min-max normalization (default)
normalized_minmax = normalize_data(raw_data)
print(f"Raw Data:       {raw_data}")
print(f"Min-Max:        {normalized_minmax}")

# Z-score normalization
normalized_zscore = normalize_data(raw_data, method='z-score')
print(f"Z-Score:        {[round(x, 4) for x in normalized_zscore]}")