import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import pandas as pd
import os
import base64

def load_model():
    """Loads the pre-trained model."""
    model_path = 'outputs/model_outputs/mildew_detector_model.h5'
    model = tf.keras.models.load_model(model_path)
    return model

def predict_mildew(model, img_array):
    """Predicts if a cherry leaf has powdery mildew and returns the confidence level."""
    predictions = model.predict(img_array)
    confidence = predictions[0][0]  # Get the model's confidence from the predictions

    if confidence < 0.5:
        confidence = 1 - confidence
        prediction_class = "Healthy"
    else:
        prediction_class = "Powdery Mildew"

    confidence_percentage = "{:.2f}%".format(confidence * 100)
    return prediction_class, confidence_percentage

def resize_image(image, target_size=(256, 256)):
    """Resizes an image to the target size."""
    return image.resize(target_size)

def display_mildew_detection():
    st.title("Cherry Leaf Mildew Detection")
    st.write("## Instructions")
    st.markdown("Download cherry leaf images from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves?rvi=1) and upload them here to detect the presence of powdery mildew.")

    model = load_model()
    uploaded_files = st.file_uploader("Choose cherry leaf images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    # Prepare an empty DataFrame to store results
    results_df = pd.DataFrame(columns=["Image Name", "Prediction", "Confidence"])

    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file).convert('RGB')
        resized_img = resize_image(img)
        img_array = np.expand_dims(np.array(resized_img) / 255.0, axis=0)
        
        prediction, confidence = predict_mildew(model, img_array)
        # Append results to the DataFrame
        results_df = results_df.append({"Image Name": uploaded_file.name, "Prediction": prediction, "Confidence": confidence}, ignore_index=True)
    
    if not results_df.empty:
        # Display the results table
        st.write("## Prediction Results")
        st.dataframe(results_df)

        # Convert DataFrame to CSV for download
        csv = results_df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="prediction_results.csv" target="_blank">Download prediction results as CSV</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    display_mildew_detection()
