import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Sample Data (Features: Size, Weight | Labels: 0 = Small Object, 1 = Large Object)
X = np.array([[1, 20], [2, 30], [3, 40], [4, 50], [5, 60], [6, 70], [7, 80], [8, 90], [9, 100], [10, 110]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Class labels (0 = Small, 1 = Large)

# Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN Model (k=3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predict on Test Data
predictions = model.predict(X_test)

# Evaluate Accuracy
accuracy = accuracy_score(y_test, predictions)
print("KNN Model Accuracy:", accuracy)

# Visualizing the Data
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", label="Data Points")
plt.xlabel("Size")
plt.ylabel("Weight")
plt.title("K-Nearest Neighbors (KNN) Classification")
plt.colorbar(label="Class (0 = Small, 1 = Large)")
plt.show()
