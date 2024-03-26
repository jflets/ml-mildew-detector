import streamlit as st

def display_project_hypothesis():
    st.title("Project Hypothesis and Validation")

    st.write("""
    ## Project Hypothesis

    At the outset of this project, we hypothesized that there are distinguishable visual markers present in cherry leaves that can accurately indicate the presence of powdery mildew infection. These markers include but are not limited to, changes in leaf color, texture, and the presence of powdery white spots or patches.

    ## Approach for Validation

    To validate this hypothesis, we employed a combination of image processing techniques and machine learning models. Initially, we conducted a comprehensive visual differentiation study to identify potential visual markers. Subsequently, we trained a convolutional neural network (CNN) model to classify the leaves as either healthy or infected based on these visual markers.

    ## Findings

    ### Visual Differentiation Study
    The visual differentiation study revealed significant visual differences between healthy and powdery mildew-infected leaves. Average images and variability analyses pointed towards distinctive color and texture patterns that could serve as markers for infection.

    ### Model Training and Evaluation
    The CNN model trained on these visual markers achieved an accuracy of [mention the accuracy], surpassing our initial performance goal. This outcome strongly supports our hypothesis that powdery mildew infection in cherry leaves can be detected through visual markers.

    ## Conclusion

    The results from both the visual study and the machine learning model validation confirm our hypothesis. We've demonstrated that it is possible to differentiate between healthy and powdery mildew-infected cherry leaves using visual markers. This finding holds promise for developing an automated tool to assist farmers and agriculturalists in early disease detection and management.
    """)

    st.write("""
    ## Next Steps

    Moving forward, we plan to refine our model further by incorporating a larger dataset and exploring more sophisticated image processing and machine learning techniques. Additionally, we aim to develop a user-friendly application that can be used in the field for real-time detection of powdery mildew in cherry leaves.
    """)

if __name__ == "__main__":
    display_project_hypothesis()
