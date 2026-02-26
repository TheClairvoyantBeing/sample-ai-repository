"""
Sentiment Analysis using Transformers
"""

from transformers import pipeline

# Loading pretrained sentiment analysis model
print("Loading sentiment analysis pipeline (this may download model weights if not present)...")
classifier = pipeline('sentiment-analysis')

# Test data
texts = [
    "I love Generative AI!",
    "This task is quite challenging.",
    "It's okay, but could be better."
]

print("\nRunning Sentiment Analysis:\n" + "-"*30)
for text in texts:
    result = classifier(text)[0]
    print(f"Text: \"{text}\"")
    print(f"  -> Label: {result['label']}, Score: {result['score']:.2%}\n")