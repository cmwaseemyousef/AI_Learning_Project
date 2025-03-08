import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load MNIST Dataset (Handwritten Digits)
mnist = keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize the Data (Scale pixels between 0 and 1)
X_train, X_test = X_train / 255.0, X_test / 255.0

# Reshape Data (CNN expects 4D: Batch, Height, Width, Channels)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# Build a Convolutional Neural Network (CNN)
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),  # Convolution Layer
    keras.layers.MaxPooling2D((2, 2)),  # Max Pooling
    keras.layers.Conv2D(64, (3, 3), activation="relu"),  # Second Convolution Layer
    keras.layers.MaxPooling2D((2, 2)),  # Second Pooling Layer
    keras.layers.Flatten(),  # Flatten 2D -> 1D
    keras.layers.Dense(128, activation="relu"),  # Fully Connected Layer
    keras.layers.Dense(10, activation="softmax")  # Output Layer (10 Classes)
])

# Compile Model
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Train Model
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# Evaluate Model
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_acc)

# Display a Sample Image
plt.imshow(X_test[0].reshape(28, 28), cmap="gray")
plt.title(f"Actual Label: {y_test[0]}")
plt.show()
