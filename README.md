# Mildew Detection in Cherry Leaves

## Project Overview
This project aims to develop a machine learning model and a supporting dashboard to differentiate between healthy cherry leaves and those infected with powdery mildew.


### Live site
Please click [here](https://jf-mildew-detector-09b8c9aef9a8.herokuapp.com) to view the live sit. Please allow time for the application to load and please open this in a new tab.

## Agile
### Kanban Board
I utilized a [Kanban Board](https://github.com/users/jflets/projects/4) to layout what needed to be completed to finish this project. Doing this kept me on track and helped break up the whole project into manageable chunks with clear objectives.

### User Stories
From 5 Epics, 9 User stories were developed. Each story was given acceptance criteria to complete and tasks to further break down each story. The full list of User Stories, separated by those completed and those pushed to a future release, is available on the project [Kanban Board](https://github.com/users/jflets/projects/4).

### Story Points
Each story was assigned story points based on your best estimation for the time/difficulty of completing each story, using the fibonacci sequence. Using the story points give me a good understanding of how long each task would take.

## How to Use the Streamlit Dashboard for Mildew Detection in Cherry Leaves

Our Streamlit dashboard is designed to provide an interactive way to explore our machine learning model's capabilities in detecting powdery mildew in cherry leaves. Here's a guide on how to navigate and use the dashboard effectively.

#### Accessing the Dashboard
1. Open a web browser and navigate to the URL of the deployed dashboard. Due to the nature of Heroku please allow some time for the application to load: https://jf-mildew-detector-09b8c9aef9a8.herokuapp.com.

#### Navigating the Dashboard
The sidebar on the left side of the dashboard serves as your main navigation menu. Here, you can select different pages to explore various aspects of the project.

#### Project Summary
- **Objective:** Get an overview of the project.
- **How to Use:** Click on "Project Summary" in the sidebar. This page provides an introduction to the project, including the dataset used, objectives, and business requirements addressed by the project.

#### Visual Differentiation Study
- **Objective:** Explore the findings from the visual differentiation study between healthy and powdery mildew-infected cherry leaves.
- **How to Use:** Select "Visual Differentiation Study" from the sidebar. This section showcases average and variability images, highlights differences between healthy and infected leaves, and presents image montages for visual comparison.

#### Mildew Detection
- **Objective:** Use the machine learning model to predict the health status of cherry leaves.
- **How to Use:** Choose "Mildew Detection" in the sidebar. Upload a cherry leaf image using the file uploader widget. After uploading, click the "Predict" button to receive the model's prediction and confidence level regarding the leaf's health status.

#### Project Hypothesis and Validation
- **Objective:** Understand the project hypothesis and how it was validated.
- **How to Use:** Navigate to "Project Hypothesis and Validation" from the sidebar. This page discusses the hypothesis behind the project and the methods used for validation, including model performance metrics.

#### Model Performance
- **Objective:** Review the performance of the machine learning model.
- **How to Use:** Click on "Model Performance" in the sidebar. This section provides graphs illustrating the model's accuracy and loss over training and validation phases, alongside a summary of its performance on the test set.

#### Additional Features
- **Interactive Elements:** Many pages include interactive elements such as buttons and checkboxes, which you can use to customize your experience.
- **Downloading Results:** On pages that provide predictions or analyses, look for options to download the results for your records.

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

## Hypothesis and Validation
- **Hypothesis**: An ML model can accurately and efficiently differentiate between healthy and powdery mildew-infected cherry leaves.
- **Validation**: The hypothesis will be validated by achieving a target accuracy of 97% in distinguishing between the two classes of leaves.

## ML Business Case
Implementing an ML model addresses the need for a scalable solution to inspect cherry leaves for powdery mildew. Success in this project can lead to broader applications across different crops, aligning with the company's goals.

## Design Document for Streamlit Dashboard

1. **Project Summary Page**
![Landing Page](/static/images/landing-page.webp)
    - **Objective**: Provide an overview of the project, dataset, and client's requirements.
    - **Components**:
        - Project introduction.
        - Dataset summary.
        - Business requirements overview.

2. **Visual Differentiation Study Page**
![Visual Differentiation Study](/static/images/vd-study.webp)
    - **Objective**: Address BR1 by showcasing the study's findings.
    - **Components**:
        - Analysis of average and variability images for each class.
        - Visual comparison between healthy and powdery mildew-infected leaves.
        - Image montage display for both classes.

3. **Mildew Detection Page**
![Mildew Detector](/static/images/detector.webp)
    - **Objective**: Fulfill BR2 by allowing users to predict the health status of cherry leaves.
    - **Components**:
        - File uploader for image prediction.
        - Display of uploaded images with prediction statements and probabilities.
        - Table of image names and prediction results with a download option.
    ![Download](/static/images/output-summary.webp)

4. **Project Hypothesis and Validation Page**
![Project hypothesis](/static/images/hypoth.webp)
    - **Objective**: Explain the project hypothesis and the methods used for validation.
    - **Components**:
        - Detailed explanation of hypothesis.
        - Validation methods and findings.

5. **Model Performance Page**
![Model Performance](/static/images/model-performance.webp)
    - **Objective**: Present the performance metrics of the developed model.
    - **Components**:
        - Accuracy and loss graphs.
        - Detailed model evaluation results.

## Bugs and or Issues
### Bugs:
 - There are currently no bugs that I am aware of in either the notebooks or the streamlit code.

### Issues during development:
 1. I had an issue when creating the ML model where i was getting under fitting. This was due to a low epoch amount leading to this issue. After some testing I settled on 15 epochs as this gave me the best balance in my ML model.

 2. When trying to deploy my application to Heroku, I ran in to an issue of having to large a slug (exceeded max slug limit of: 500Mb) I had a slugignore but was till well over the limit. After analyzing the build logs i realized that the packages bing installed where very large and had multiple additional dependencies leading to a larger slug. To resolve this i decided to adjust my decencies and slim them down to only the main ones I need, this made a slight difference. I then decided to add all static images and files not used in the deployment to the slugignore and again this help some what but i was still over the limit.
 I then realized that it was the fact that i was using the full version of tensorflow rather than just tensorflow-cpu this was casing the slug size issue. I decided to split my requirements into a development requirements and a deployment requirements, as the application does not use all the same dependencies as the jupyter notebooks I then used tensorflow-cpu as it is much smaller than the full tensorflow and this fixed the slug size issue.

## Deployment

### Deployment to Heroku

**The live link to the app:** Replace `YOUR_APP_NAME` with your actual app name in the URL `https://YOUR_APP_NAME.herokuapp.com/`. Make sure your `runtime.txt` file specifies a Python version compatible with the Heroku-20 stack.

**Deploying your Streamlit app on Heroku involves the following steps:**

1. **Prepare Your Application**
   - Ensure your application includes a `requirements.txt` file listing all necessary libraries, a `Procfile` with commands to launch your app, and optionally, a `setup.sh` file for configuring Streamlit.
   - Create a `runtime.txt` to specify the Python version. Make sure it is compatible with Heroku-20 stack supported versions.

2. **Log in to Heroku**
   - If you haven't already, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and log in using the command `heroku login`.

3. **Create an App on Heroku**
   - Use the Heroku CLI to create a new app: `heroku create YOUR_APP_NAME`. This name will be part of your app's URL.

4. **Set Up GitHub Integration (Optional)**
   - On the Heroku dashboard, you can connect your GitHub repository to Heroku for automatic deployments. Navigate to the "Deploy" tab in your Heroku app's dashboard, select "GitHub" as the deployment method, search for your repository, and connect.

5. **Deploy Your Application**
   - If you're deploying manually using Git, set Heroku as a remote for your repository: `heroku git:remote -a YOUR_APP_NAME`.
   - Push your application to Heroku: `git push heroku master`. If you're working on a different branch, use `git push heroku YOUR_BRANCH_NAME:master`.

6. **Access Your Deployed Application**
   - After a successful deployment, you can access your app by clicking the "Open App" button on the Heroku dashboard or visiting `https://YOUR_APP_NAME.herokuapp.com/` directly.

7. **Managing Slug Size**
   - If your slug size is too large, consider using a `.slugignore` file to exclude files and directories that aren't necessary for running your app on Heroku. This can help reduce the slug size and speed up deployment times.

**Troubleshooting Deployment Issues**
- Ensure all dependencies listed in your `requirements.txt` are available and not causing conflicts.
- Make sure to separate your dependencies with a `dev_requirements.txt` folder and your main one, this will reduce unnecessary dependencies that will inflate the final file size on Heroku, leading to errors.
- Check your `Procfile` and `setup.sh` (if used) for any errors in commands.
- Review the build logs in Heroku's dashboard for specific error messages that can guide troubleshooting.

## Main Data Analysis and Machine Learning Libraries
- ### TensorFlow-CPU and Keras
    - Usage: TensorFlow-CPU, along with its high-level API Keras, forms the backbone of our machine learning model. We use it to construct, train, and evaluate a deep learning model capable of classifying cherry leaves as healthy or infected with powdery mildew.
- ### NumPy
    - Usage: NumPy is used for efficient numerical computations, especially for array manipulations which are essential when processing images for our model.
- ### Pandas
    - Usage: Pandas provides convenient data structures and functions for data analysis tasks. In this project, it's primarily used for handling and displaying data in tabular form, which is helpful for summarizing the model's performance metrics.
- ### Matplotlib
    - Usage: Matplotlib is a plotting library used for creating static, interactive, and animated visualizations in Python. It's used extensively in this project to plot learning curves, model performance, and augmented images.
- ### Pillow
    - Usage: Pillow, the Python Imaging Library, adds image processing capabilities to our Python interpreter. In this project, it is crucial for loading, processing, and manipulating images before they are fed into the machine learning model for training and predictions. Pillow's functionality enables us to apply necessary pre-processing steps to the images, such as resizing, which directly impacts the model's performance.
- ### Streamlit
    - Usage: Streamlit is an open-source app framework for Machine Learning and Data Science teams. It's used to quickly build interactive web applications for our model's visual differentiation study and mildew detection functionality.


## Testing

| **Feature**       | **Expected Outcome**                                                       | **Testing Performed**                                            | **Result**                            | **Pass/Fail** |
|:-----------------:|:--------------------------------------------------------------------------:|:----------------------------------------------------------------:|:-------------------------------------:|:-------------:|
| Nav links         | Nav links should load the corresponding page                               | Click the nav links                                              | All links open the appropriate pages  | Pass          |
| Links             | Links should load the appropriate content                                  | Click the kaggle link                                       | Link loads the kaggle mildew data page            | Pass          |
| Show information checkboxes         | Checkboxes should display the appropriate information when clicked | Click the checkboxes                                                   | Displays the appropriate content           | Pass          |
| Mildew detection page | User should be able to upload multiple images and each images should be displayed and should display weather the leaf is healthy or infected with a confidence percentage. Then there should be a summary at the bottom of all the images and their results.                                | Upload multiple images to mildew detector | All images are displayed with their results and the summary is displayed at the bottom | Pass          |
| Upload image button | Clicking this button should allow the user to select an image from their pc                                | Click the upload image button | Loads a popup allowing user to select images from their pc | Pass          |
| Download prediction link | Clicking this link should allow the user to download the prediction data into a csv file                                | Click the download prediction results link | Prediction data is downloaded as a csv | Pass          |
| Add new images to mildew detection when there are already images  | User should be able to upload a new image while there are already images loaded                                 | Upload a new image while there are already images loaded | New image is displayed and results are added to the summary and the old images are retained  | Pass          |
| Remove image "X" button             | This button should remove an image from the detector page and results from the summary                                  | Click the "X" button                                       | Image and results are removed     | Pass          |

## Credits
### ML Model
- I used a combination of the ML Walkthrough project and the Churnometer Project from [Code Institute](https://codeinstitute.net) as a guide on how the model should be structured and the steps that should be taken in order to get a working ML model.

### Dashboard design
- I used a combination of the ML Walkthrough project and the Churnometer Project from [Code Institute](https://codeinstitute.net) as a guide for the dashboard.
- I used the [Streamlit](https://blog.streamlit.io/introducing-theming/) documentation on how to change the themes.
- I also used [Coolors](https://coolors.co/) for generating the colors.

### Content
- Dataset and project idea inspired by [Kaggle Cherry Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

### Media
- Images used in the dashboard are sourced from the Kaggle dataset mentioned above.
- I used [cloud convert](https://cloudconvert.com/png-to-webp) to change png's to webp so keep the file sizes down.

## Acknowledgements
I would like to thank [Code Institute](https://codeinstitute.net) for their help and guidance.
