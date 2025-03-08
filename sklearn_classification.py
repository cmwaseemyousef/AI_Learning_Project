import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample Data (Features & Labels)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # Features
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Labels (0 = Class A, 1 = Class B)

# Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on Test Data
predictions = model.predict(X_test)

# Evaluate Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)
