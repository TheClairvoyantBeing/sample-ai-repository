"""
Week 6 — ML Classification + Flask API Demo
Part 1: Logistic Regression with classification report
Part 2: Flask REST API serving predictions
Run:  python weekly-reports/week-6/ml_api_demo.py
"""

import json
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# ═════════════════════════════════════════════════════════
# PART 1: LOGISTIC REGRESSION CLASSIFIER
# ═════════════════════════════════════════════════════════

print("=" * 60)
print("  🤖  WEEK 6 — MACHINE LEARNING CLASSIFICATION REPORT")
print("=" * 60)

# ── Generate synthetic customer churn dataset ──
X, y = make_classification(
    n_samples=500, n_features=6, n_informative=4,
    n_redundant=1, n_classes=2, random_state=42,
    weights=[0.6, 0.4]
)

feature_names = [
    "Usage_Hours", "Support_Tickets", "Contract_Months",
    "Monthly_Charge", "Satisfaction_Score", "Logins_Per_Week"
]

class_names = ["Retained", "Churned"]

# ── 70/30 Train-Test Split ──
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

print(f"\n  📊 Dataset: Customer Churn Prediction")
print(f"  ├── Total Samples:   {len(X)}")
print(f"  ├── Training Set:    {len(X_train)} (70%)")
print(f"  ├── Testing Set:     {len(X_test)} (30%)")
print(f"  ├── Features:        {len(feature_names)}")
print(f"  └── Classes:         {class_names}")

# ── Train Logistic Regression ──
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)

print(f"\n  ✅ Model trained successfully!")
print(f"  📈 Accuracy: {accuracy:.2%}")

# ── Classification Report ──
print("\n  ┌────────────────────────────────────────────────┐")
print("  │         CLASSIFICATION REPORT                  │")
print("  └────────────────────────────────────────────────┘\n")
print(classification_report(y_test, y_pred, target_names=class_names))

# ── Confusion Matrix ──
cm = confusion_matrix(y_test, y_pred)
print("  ┌────────────────────────────────────────────────┐")
print("  │         CONFUSION MATRIX                       │")
print("  └────────────────────────────────────────────────┘")
print(f"\n                   Predicted")
print(f"                Retained  Churned")
print(f"  Actual Retained  {cm[0][0]:>5}    {cm[0][1]:>5}")
print(f"  Actual Churned   {cm[1][0]:>5}    {cm[1][1]:>5}")

# ═════════════════════════════════════════════════════════
# PART 2: FLASK REST API (prints sample JSON response)
# ═════════════════════════════════════════════════════════

print("\n\n" + "=" * 60)
print("  🌐  FLASK REST API — SAMPLE RESPONSE")
print("=" * 60)

# Simulate a prediction API response
sample_input = X_test[0].tolist()
sample_pred = model.predict([X_test[0]])[0]
sample_proba = model.predict_proba([X_test[0]])[0].tolist()

api_response = {
    "status": 200,
    "endpoint": "/api/v1/predict",
    "method": "POST",
    "request": {
        "features": {name: round(val, 3) for name, val in zip(feature_names, sample_input)}
    },
    "response": {
        "prediction": class_names[sample_pred],
        "confidence": {
            class_names[0]: f"{sample_proba[0]:.1%}",
            class_names[1]: f"{sample_proba[1]:.1%}",
        },
        "model": "LogisticRegression",
        "version": "1.0.0"
    }
}

print(f"\n  POST /api/v1/predict  →  200 OK\n")
print(json.dumps(api_response, indent=2))

print("\n" + "=" * 60)
print("  ✅ ML + API demo completed!")
print("=" * 60)
