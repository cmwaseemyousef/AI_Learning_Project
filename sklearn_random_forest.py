import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample Data (Features: Age, Salary | Labels: 0 = No Buy, 1 = Buy)
X = np.array([[25, 30000], [30, 40000], [35, 50000], [40, 60000], [45, 70000], [50, 80000],
              [55, 90000], [60, 100000], [65, 110000], [70, 120000]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Class labels (0 = No Buy, 1 = Buy)

# Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model (Using 10 Decision Trees)
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Predict on Test Data
predictions = model.predict(X_test)

# Evaluate Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Random Forest Accuracy:", accuracy)

# Feature Importance Visualization
importance = model.feature_importances_
plt.bar(["Age", "Salary"], importance, color=["blue", "green"])
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance in Random Forest")
plt.show()
