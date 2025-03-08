import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Sample Data (Features: Word Count, Special Characters | Labels: 0 = Not Spam, 1 = Spam)
X = np.array([[10, 2], [20, 5], [30, 7], [40, 10], [50, 12], [60, 14], [70, 16], [80, 18], [90, 20], [100, 22]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Labels (0 = Not Spam, 1 = Spam)

# Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM Model
model = SVC(kernel="linear")  # Linear Kernel for Simple Classification
model.fit(X_train, y_train)

# Predict on Test Data
predictions = model.predict(X_test)

# Evaluate Accuracy
accuracy = accuracy_score(y_test, predictions)
print("SVM Model Accuracy:", accuracy)

# Visualizing Decision Boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", label="Data Points")
plt.xlabel("Word Count")
plt.ylabel("Special Characters")
plt.title("Support Vector Machine (SVM) Classification")
plt.colorbar(label="Class (0 = Not Spam, 1 = Spam)")
plt.show()
