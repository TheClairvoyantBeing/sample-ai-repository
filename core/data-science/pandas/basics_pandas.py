# ============================================================
# Pandas — DataFrames for AI & Data Science
# Demonstrates: DataFrame creation, info, statistics,
#               value_counts, and conditional filtering.
# ============================================================

import pandas as pd

print("=" * 50)
print("PANDAS FOR AI")
print("=" * 50)

# ── 1. Create a sentiment analysis dataset ───────────────────
# Each row = one text sample with its sentiment label, confidence score, and length
data = {
    'text':      ['I love this', 'This is a bad product', 'Great Service', 'He is a Terrible person'],
    'sentiment': ['positive', 'negative', 'positive', 'negative'],
    'score':     [0.95, 0.93, 0.89, 0.92],
    'length':    [11, 21, 13, 23]
}

df = pd.DataFrame(data)     # convert dict → DataFrame (tabular format)

# ── 2. View the full dataset ────────────────────────────────
print("\n1. Dataset")
print(df)

# ── 3. DataFrame metadata ───────────────────────────────────
# .info() shows column names, types, and non-null counts
print("\n2. Info")
print(df.info())

# ── 4. Descriptive statistics ───────────────────────────────
# .describe() gives count, mean, std, min, max for numeric columns
print("\n3. Statistics")
print(df.describe())

# ── 5. Value counts — how many of each sentiment? ───────────
print("\n4. Value Counts")
print("Sentiment Distribution:")
print(df['sentiment'].value_counts())          # positive: 2, negative: 2

# ── 6. Filter rows by condition ─────────────────────────────
# Select only rows where confidence score > 0.90
print("\n5. Filtering (score > 0.90)")
high_score = df[df['score'] > 0.90]
print("High Confidence Samples:")
print(high_score)