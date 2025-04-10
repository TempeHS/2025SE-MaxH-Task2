# Student Performance Predictor: Insights into Student Performance and Contributing Factors

!! This model only serves as a prediction and does not account for student's guarenteed results.

This repository contains a Machine Learning (ML) project aimed at analyzing and predicting student performance based on various contributing factors such as socioeconomic background, academic history, and extracurricular activities. The project leverages educational datasets to build predictive models that can help educators, policymakers, and students understand the key drivers of academic success and identify areas for improvement.

# Business Problem

- Educational institutions and policymakers often struggle to identify the key factors that influence student performance. Understanding how factors such as socioeconomic background, study habits, and extracurricular activities impact academic outcomes can help educators design targeted interventions and improve overall student success.

- This project aims to provide actionable insights into the factors that contribute to student performance and develop predictive models to forecast academic outcomes based on these factors.

# Machine Learning Problem

- The goal is to develop a Machine Learning model that predicts student exam scores based on several input features.

# Success Metrics

To evaluate the performance of the machine learning model, the following success metrics will be used:

- Does the model generalise well to training data, testing data and new data that has been caputured during operation
- Does the model score a low Mean Squared Error(MSE)
- Model is updateable and continuously able to be retrained with user input data and results

# Data Overview

- I have sourced a raw validated dataset that is saved in the CSV file [1.1.4.Student_Scores_Data.csv](/1.Model_Development/1.1.Data_Wrangling/1.1.4.Student_Scores_Data.csv).

- The data columns are:
  | Column | Description |
  |----------------------------|-------------------------------------------------------------------------------------------------|
  | Hours_Studied | Number of hours the student studied per week. |
  | Attendance | Percentage of classes attended by the student. |
  | Parental_Involvement | Level of parental involvement in the student's education (e.g., Low, Medium, High). |
  | Access_to_Resources | Availability of educational resources (e.g., books, internet, study materials). |
  | Extracurricular_Activities | Participation in extracurricular activities (e.g., sports, music, clubs). |
  | Sleep_Hours | Average number of hours the student sleeps per night. |
  | Previous_Scores | Scores from previous exams or assessments. |
  | Motivation_Level | Self-reported motivation level (e.g., Low, Medium, High). |
  | Internet_Access | Whether the student has access to the internet at home (e.g., Yes/No). |
  | Tutoring_Sessions | Number of tutoring sessions attended by the student. |
  | Family_Income | Family's annual income (e.g., Low, Med, High). |
  | Teacher_Quality | Quality of teaching as rated by students (e.g., Low, Medium, High). |
  | School_Type | Type of school attended (e.g., Public or Private). |
  | Peer_Influence | Influence of peers on the student's academic performance (e.g., Positive, Neutral, Negative). |
  | Physical_Activity | Amount of physical activity per week (e.g., hours). |
  | Learning_Disabilities | Whether the student has any diagnosed learning disabilities (e.g., Yes/No). |
  | Parental_Education_Level | Highest education level attained by the parents (e.g., High school, College, Post-Grad). |
  | Distance_from_Home | Distance from the student's home to school (e.g., Near, Moderate, Far). |
  | Gender | Gender of the student (e.g., Male/Female). |
  | Exam_Score | Final exam score of the student (target variable). |

# How to execute program

- Install required dependencies with:

  ```bash
    pip install -r requirements.txt
  ```

- Numerically go through jupyter notebooks starting from Data Preview until you are up to Model Deployment.
- After wrangling data, engineering features, evaluating the most accurate model and saving the model in 2.Operations/operations_models deploy the API using:

  ```bash
  python api.py
  ```

- And in a new terminal

  ```bash
  python main.py
  ```

- You will be able to open API in the browser on port http://127.0.0.1:5000 and let others make predictions for their upcoming exam.

- [TempeHS Jupyter-Notebook template](https://github.com/TempeHS/TempeHS_Jupyter-Notebook_DevContainer)
