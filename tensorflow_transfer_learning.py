import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt

# Load Pre-Trained Model (MobileNetV2)
model = MobileNetV2(weights="imagenet")  # Uses pre-trained ImageNet weights

# Load and Preprocess an Image
img_path = "cat.jpg"  # Replace with any image file
img = image.load_img(img_path, target_size=(224, 224))  # Resize image
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match model input
img_array = preprocess_input(img_array)  # Normalize image

# Make Prediction
predictions = model.predict(img_array)
decoded_preds = decode_predictions(predictions, top=3)[0]  # Get top 3 predictions

# Display Image and Predictions
plt.imshow(img)
plt.axis("off")
plt.title(f"Predicted: {decoded_preds[0][1]} ({decoded_preds[0][2]*100:.2f}%)")
plt.show()

# Print Predictions
for i, (imagenet_id, label, score) in enumerate(decoded_preds):
    print(f"{i+1}: {label} ({score*100:.2f}%)")
