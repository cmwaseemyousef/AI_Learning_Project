import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score

# Sample Data (Features: Age, Salary | Labels: 0 = No Buy, 1 = Buy)
X = np.array([[25, 30000], [30, 40000], [35, 50000], [40, 60000], [45, 70000], [50, 80000],
              [55, 90000], [60, 100000], [65, 110000], [70, 120000]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Class labels (0 = No Buy, 1 = Buy)

# Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict on Test Data
predictions = model.predict(X_test)

# Evaluate Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Decision Tree Accuracy:", accuracy)

# Visualizing the Decision Tree
plt.figure(figsize=(10, 6))
tree.plot_tree(model, feature_names=["Age", "Salary"], class_names=["No Buy", "Buy"], filled=True)
plt.show()
