import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load MNIST Dataset (Handwritten Digits)
mnist = keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize the Data (Scaling between 0 and 1)
X_train, X_test = X_train / 255.0, X_test / 255.0

# Build a Simple Neural Network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Input Layer (Flatten 28x28 images)
    keras.layers.Dense(128, activation="relu"),  # Hidden Layer (128 Neurons, ReLU Activation)
    keras.layers.Dense(10, activation="softmax")  # Output Layer (10 Classes, Softmax Activation)
])

# Compile Model
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Train Model
model.fit(X_train, y_train, epochs=5)

# Evaluate Model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_acc)

# Display a Sample Image
plt.imshow(X_test[0], cmap="gray")
plt.title(f"Actual Label: {y_test[0]}")
plt.show()
