import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image

def display_model_performance():
    st.title("Model Performance")

    st.write("## Model Training Metrics")
    st.write("""
    This section outlines the performance of the machine learning model trained to classify cherry leaves as either healthy or infected by powdery mildew. We'll look at the accuracy and loss during training and validation phases, as well as the model's final performance on the test set.
    """)

    # Update base path for model outputs
    model_outputs_dir = "outputs/model_outputs"
    

    # Load and display the training accuracy and loss plots
    training_accuracy_path = os.path.join(model_outputs_dir, "training_accuracy.png")
    training_loss_path = os.path.join(model_outputs_dir, "training_loss.png")

    if os.path.exists(training_accuracy_path) and os.path.exists(training_loss_path):
        training_accuracy = Image.open(training_accuracy_path)
        training_loss = Image.open(training_loss_path)

        col1, col2 = st.columns(2)
        with col1:
            st.image(training_accuracy, caption="Training Accuracy")
        with col2:
            st.image(training_loss, caption="Training Loss")
    else:
        st.error("Training accuracy and loss plots are not available.")

    st.write("## Test Set Performance")
    st.write("""
    After training, the model was evaluated on a separate test set to assess its generalization ability. Here are the results:
    """)

    # Update path for test set performance metrics (assuming it's saved as a .pkl for demonstration)
    test_performance_path = os.path.join(model_outputs_dir, "test_results.pkl")
    
    if os.path.exists(test_performance_path):
        # Assuming the test performance data is saved as a pickle file
        test_performance_df = pd.read_pickle(test_performance_path)
        st.dataframe(test_performance_df)
    else:
        st.error("Test set performance data is not available.")

if __name__ == "__main__":
    display_model_performance()
