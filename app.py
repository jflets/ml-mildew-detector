import streamlit as st
from app_pages.page_project_summary import display_project_summary
from app_pages.page_visual_differentiation_study import display_visual_differentiation_study
from app_pages.page_mildew_detection import display_mildew_detection
from app_pages.page_project_hypothesis import display_project_hypothesis
from app_pages.page_model_performance import display_model_performance

# Set page config
st.set_page_config(page_title="Mildew Detection in Cherry Leaves", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
options = ["Project Summary", "Visual Differentiation Study", "Mildew Detection", "Project Hypothesis and Validation", "Model Performance"]
selection = st.sidebar.radio("Go to", options)

# Page display
if selection == "Project Summary":
    display_project_summary()
elif selection == "Visual Differentiation Study":
    display_visual_differentiation_study()
elif selection == "Mildew Detection":
    display_mildew_detection()
elif selection == "Project Hypothesis and Validation":
    display_project_hypothesis()
elif selection == "Model Performance":
    display_model_performance()
