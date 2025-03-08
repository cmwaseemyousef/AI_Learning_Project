import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample Training Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Features (Independent Variable)
y = np.array([10, 20, 25, 30, 50])  # Target (Dependent Variable)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Values
predictions = model.predict(X)

# Plot Results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, predictions, color="red", label="Regression Line")
plt.xlabel("X Values")
plt.ylabel("Y Predictions")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()
