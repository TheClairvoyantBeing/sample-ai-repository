from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import numpy as np

print("="*60)
print("SCIKIT LEARN CLASSIFICATION")
print("="*60)

np.random.seed(42)

# Feature [hours studied, previous score]
x = np.array([
    [2,45],[3,55],[5,65],[7,75],[8,85],[1,40],[4,60],[6,70],[9,90],[10,95],[2.5,50],[5.5,68],[7.5,78],[8.5,88],[9.5,92]
])

# Labels: 0 = Fail, 1 = Pass
y = np.array([0,0,1,1,1,0,1,1,1,1,0,1,1,1,1])

print(f"\n1. DATASET")
print(f"Samples: {len(x)}")
print(f"Features: {x.shape[1]}")
print(f"First 5 samples:")
print(x[:5])

print("\n2. TRAINING")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = LogisticRegression()
model.fit(x_train_scaled, y_train)
print("Model trained successfully.")

print("\n3. EVALUATION")
y_pred = model.predict(x_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))