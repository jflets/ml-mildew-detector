import streamlit as st
from PIL import Image
import os

def display_visual_differentiation_study():
    st.title("Visual Differentiation Study for Cherry Leaves")

    st.write("""
    This section explores the visual differentiation between healthy cherry leaves and those infected with powdery mildew. Through various visual analyses, we aim to understand the distinguishing features that can aid in detection and classification.
    """)

    # Base path for generated images
    generated_images_dir = "outputs/data_visualization/v1/generated_images"

    # Checkbox for displaying average and variability images
    if st.checkbox("Show Average and Variability Images"):
        st.subheader("Average and Variability Images")
        st.write("""
        Average images represent the mean visual appearance of leaves within each category, while variability images show the spread of differences across the dataset, highlighting the most common features.
        """)

        # Display images
        avg_healthy_path = os.path.join(generated_images_dir, "healthy_average.png")
        avg_powdery_mildew_path = os.path.join(generated_images_dir, "powdery_mildew_average.png")
        var_healthy_path = os.path.join(generated_images_dir, "healthy_variability.png")
        var_powdery_mildew_path = os.path.join(generated_images_dir, "powdery_mildew_variability.png")

        avg_healthy = Image.open(avg_healthy_path)
        avg_powdery_mildew = Image.open(avg_powdery_mildew_path)
        var_healthy = Image.open(var_healthy_path)
        var_powdery_mildew = Image.open(var_powdery_mildew_path)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(avg_healthy, caption="Average Healthy Leaf")
        with col2:
            st.image(avg_powdery_mildew, caption="Average Powdery Mildew Leaf")
        with col3:
            st.image(var_healthy, caption="Variability in Healthy Leaves")
        with col4:
            st.image(var_powdery_mildew, caption="Variability in Powdery Mildew Leaves")
        
        st.warning("""
        * The average images offer a clear distinction between healthy and powdery mildew-infected leaves, notably in terms of color and texture patterns. This suggests potential visual markers for classification.
        * Variability images indicate a significant range of appearance within each class, emphasizing the importance of a robust classification model capable of handling intra-class variation.
        """)

    # Checkbox for displaying the difference between average images
    if st.checkbox("Show Difference Between Average Images"):
        st.subheader("Difference Between Average Images")
        st.write("""
        This image highlights the differences between the average appearances of healthy and infected leaves, emphasizing features that are potentially useful for classification.
        """)
        difference_path = os.path.join(generated_images_dir, "difference_between_averages.png")
        difference_image = Image.open(difference_path)
        st.image(difference_image, caption="Difference Between Average Images")
        st.warning("""
        * The difference between average images accentuates the unique characteristics distinguishing healthy leaves from those with powdery mildew. These visual cues could be crucial for developing accurate detection algorithms.
        """)

    # Checkbox for displaying image montages
    if st.checkbox("Show Image Montages"):
        st.subheader("Image Montages")
        st.write("""
        Image montages provide a comprehensive view of the dataset, showcasing a variety of leaves from each category. This helps in understanding the diversity within the classes.
        """)
        montage_healthy_path = os.path.join(generated_images_dir, "healthy_montage.png")
        montage_powdery_mildew_path = os.path.join(generated_images_dir, "powdery_mildew_montage.png")

        montage_healthy = Image.open(montage_healthy_path)
        montage_powdery_mildew = Image.open(montage_powdery_mildew_path)

        col1, col2 = st.columns(2)
        with col1:
            st.image(montage_healthy, caption="Montage of Healthy Leaves")
        with col2:
            st.image(montage_powdery_mildew, caption="Montage of Powdery Mildew Leaves")
        st.warning("""
        * Montages reveal the complexity and variability within each class, underscoring the challenge of distinguishing mildew-infected leaves from healthy ones based solely on visual inspection.
        """)
