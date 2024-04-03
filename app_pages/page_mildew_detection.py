import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

def load_model():
    """Loads the pre-trained model."""
    model_path = 'outputs/model_outputs/mildew_detector_model.h5'
    model = tf.keras.models.load_model(model_path)
    return model

def predict_mildew(model, img_array):
    """Predicts if a cherry leaf has powdery mildew and returns the confidence level."""
    predictions = model.predict(img_array)
    confidence = predictions[0][0]  # Get the model's confidence from the predictions

    # Adjust confidence based on the predicted class
    if confidence < 0.5:
        confidence = 1 - confidence
        prediction_class = "Healthy"
    else:
        prediction_class = "Powdery Mildew"

    # Convert confidence to a formatted percentage string
    confidence_percentage = "{:.2f}%".format(confidence * 100)

    return prediction_class, confidence_percentage

def resize_image(image, target_size=(256, 256)):
    """Resizes an image to the target size."""
    return image.resize(target_size)

def display_mildew_detection():
    st.title("Cherry Leaf Mildew Detection")
    st.write("## Instructions")
    st.markdown("Download cherry leaf images from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves?rvi=1) and upload them here to detect the presence of powdery mildew.")

    # Load the pre-trained model
    model = load_model()

    uploaded_file = st.file_uploader("Choose a cherry leaf image", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert('RGB')
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            resized_img = resize_image(img)
            img_array = np.expand_dims(np.array(resized_img) / 255.0, axis=0)
            
            prediction, confidence = predict_mildew(model, img_array)
            st.write(f"Prediction: **{prediction}**")
            st.write(f"Confidence: **{confidence}**")

if __name__ == "__main__":
    display_mildew_detection()
