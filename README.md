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

# MLOps Pipeline Automation for Student Exam Score Predictor

This repository contains a Machine Learning (ML) project aimed at automating the development, deployment, and operation of a predictive model for student exam scores. The project is divided into two main phases: **Model Development** and **Operations**.

---

## 1. MLOps Model Development Phase

### 1.1 Data Wrangling

- The [Data Preview Jupyter Notebook](/1.Model_Development/1.1.Data_Wrangling/data_preview.ipynb) provides an overview and understanding of the dataset using snapshots, data summaries, graphs, and descriptive statistics.
- The [Data Wrangling Jupyter Notebook](/1.Model_Development/1.1.Data_Wrangling/data_wrangling.ipynb) demonstrates the data wrangling processes using the Pandas library and Matplotlib.
- The [Data Records Documentation](/1.Model_Development/1.1.Data_Wrangling/data.records.md) contains detailed documentation of all scaling and encoding steps performed during data wrangling and feature engineering.

### 1.2 Feature Engineering

- The [Feature Engineering Jupyter Notebook](/1.Model_Development/1.2.Feature_Engineering/feature_engineering.ipynb) shows how new features were created or existing ones were modified to improve model performance.

### 1.3 Model Training

- The [Splitting Training and Testing Data Jupyter Notebook](/1.Model_Development/1.3.Model_Training/split_training_and_testing_data.ipynb) explains how the dataset was divided into training and testing sets for model evaluation.
- The [Linear Regression Jupyter Notebook](/1.Model_Development/1.3.Model_Training/linear_regression.ipynb) demonstrates how a linear regression model was trained using the engineered features to predict student exam scores.

### 1.4 Model Testing and Validation

- The [Model Testing and Validation Jupyter Notebook](/1.Model_Development/1.4.Model_Testing_and_Validation/model_evaluation.ipynb) shows how the model was evaluated, tested, and validated using a separate test dataset to refine its performance.

---

## 2. MLOps Operations Phase

### How to Use the Model

#### Running Required Files

1. **Start the API**:
   Navigate to the `2.Operations` directory and run the API server:
   ```bash
   cd 2.Operations
   python api.py
   ```

2. **Start the Web Application**:
   In a new terminal, navigate to the `2.Operations` directory and run the main application:
   ```bash
   cd 2.Operations
   python main.py
   ```

3. **Access the Application**:
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the Student Exam Score Predictor.

---

## Disclaimer

**Note:** The results provided by this model are only predictions and should not be taken as guaranteed marks. Please use them as guidance only.

---

## Dependencies

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

---

## Acknowledgments

This project was developed to provide insights into student performance and help educators and policymakers make data-driven decisions.