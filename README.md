# Mildew Detection in Cherry Leaves

## Project Overview
This project aims to develop a machine learning model and a supporting dashboard to differentiate between healthy cherry leaves and those infected with powdery mildew. The project fulfills two main business requirements:
1. Conduct a study to visually differentiate a healthy cherry leaf from one infected with powdery mildew.
2. Predict if a cherry leaf is healthy or contains powdery mildew.

## Dataset
The dataset used in this project contains images of cherry leaves, categorized into healthy and powdery mildew-infected classes. [Dataset source](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

## Business Requirements
### BR1: Visual Differentiation Study
- Average and variability images analysis for each class.
- Differences between average healthy and powdery mildew-infected leaves.
- Image montage for each class.

### BR2: Mildew Detection
- Develop a binary classification model using Neural Networks.
- The model inputs cherry leaf images, predicting their health status.

## Dashboard
The project dashboard provides:
- A project summary including dataset information and client requirements.
- Visual differentiation study findings.
- Mildew detection functionality with image upload and prediction results.
- Hypothesis validation and model performance metrics.

## Model
The binary classification model aims for a performance goal of 97% accuracy, ensuring high-quality predictions that benefit the client by preventing the distribution of compromised products.

## Ethical Considerations
Data is provided under an NDA, restricting its sharing to officially involved professionals.

## Setup and Installation
Instructions on setting up the project environment and running the dashboard.

## Usage
Guidelines on how to navigate and use the dashboard functionalities.

## Contributions
Details on how to contribute to the project.

## License
Project license information.

### Design Document for Streamlit Dashboard

Your Streamlit dashboard design document can follow this structure:

1. **Project Summary Page**
    - **Objective**: Provide an overview of the project, dataset, and client's requirements.
    - **Components**:
        - Project introduction.
        - Dataset summary.
        - Business requirements overview.

2. **Visual Differentiation Study Page**
    - **Objective**: Address BR1 by showcasing the study's findings.
    - **Components**:
        - Analysis of average and variability images for each class.
        - Visual comparison between healthy and powdery mildew-infected leaves.
        - Image montage display for both classes.

3. **Mildew Detection Page**
    - **Objective**: Fulfill BR2 by allowing users to predict the health status of cherry leaves.
    - **Components**:
        - File uploader for image prediction.
        - Display of uploaded images with prediction statements and probabilities.
        - Table of image names and prediction results with a download option.

4. **Project Hypothesis and Validation Page**
    - **Objective**: Explain the project hypothesis and the methods used for validation.
    - **Components**:
        - Detailed explanation of hypothesis.
        - Validation methods and findings.

5. **Model Performance Page**
    - **Objective**: Present the performance metrics of the developed model.
    - **Components**:
        - Accuracy and loss graphs.
        - Detailed model evaluation results.