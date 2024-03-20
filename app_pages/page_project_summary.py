import streamlit as st

def display_project_summary():
    st.title("Project Summary: Mildew Detection in Cherry Leaves")

    st.markdown("""
    ## Project Overview
    This project aims to develop a machine learning model capable of distinguishing between healthy and powdery mildew-infected cherry leaves. Utilizing a dataset of cherry leaf images, we seek to automate the process of identifying mildew presence, aiding in agricultural quality control and disease management.

    ## Dataset Summary
    The dataset comprises images of cherry leaves categorized into two classes: healthy and powdery mildew-infected. These high-resolution images provide the foundation for training our classification model, enabling it to learn the distinguishing features of each class.

    ## Business Requirements
    1. **Visual Differentiation Study**: Conduct a study to visually differentiate between healthy and powdery mildew-infected cherry leaves.
    2. **Mildew Detection**: Predict whether a cherry leaf is healthy or contains powdery mildew, facilitating early intervention and treatment.

    ## Success Metrics
    A successful outcome for this project is the development of a model that achieves at least 97% accuracy in classifying cherry leaves, thereby ensuring reliability and effectiveness in detecting powdery mildew.
    """)

    st.markdown("""
    ## Client Benefits
    - **Quality Assurance**: Ensuring the quality and health of cherry crops by early detection of powdery mildew.
    - **Efficiency**: Reducing manual inspection time and allowing for more rapid responses to disease outbreaks.
    - **Economic Impact**: Minimizing the economic losses associated with powdery mildew through timely intervention.
    """)

    # st.image("path/to/overview_image.jpg", caption="Cherry Leaves: Healthy vs Powdery Mildew-Infected", use_column_width=True)

    st.markdown("""
    ## Next Steps
    Explore the dashboard to view the study findings on visual differentiation, try out the mildew detection feature, and review our model's performance metrics.
    """)
