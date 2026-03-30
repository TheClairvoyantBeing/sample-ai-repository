# ============================================================
# Sentiment Analysis using Hugging Face Transformers
# Uses a pretrained NLP model to classify text as
# POSITIVE or NEGATIVE with a confidence score.
#
# Dependencies: pip install transformers torch
# ============================================================

"""
Sentiment Analysis Pipeline

Uses Hugging Face's `pipeline('sentiment-analysis')` which downloads
a pretrained DistilBERT model fine-tuned on SST-2 (Stanford Sentiment
Treebank). The model classifies input text as POSITIVE or NEGATIVE.

Usage:
    python sentiment_analyzer.py
"""

from transformers import pipeline

# ── Initialize the sentiment analysis pipeline ──────────────
# The first run will download model weights (~260 MB) from Hugging Face Hub.
# Subsequent runs use the cached model.
print("Loading sentiment analysis pipeline (this may download model weights if not present)...")
classifier = pipeline('sentiment-analysis')

# ── Test data — a mix of positive, negative, and neutral text ──
texts = [
    "I love Generative AI!",
    "This task is quite challenging.",
    "It's okay, but could be better."
]

# ── Run inference on each text and print results ────────────
print("\nRunning Sentiment Analysis:\n" + "-" * 30)
for text in texts:
    result = classifier(text)[0]              # returns a list; take the first result
    label = result['label']                   # 'POSITIVE' or 'NEGATIVE'
    score = result['score']                   # confidence score (0.0 – 1.0)
    print(f"Text: \"{text}\"")
    print(f"  -> Label: {label}, Score: {score:.2%}\n")