# Multiple Linear Regression Practice Project

**Problem Statement**
This project aims to practice implementing and evaluating a multiple linear regression model using Python. The dataset used for this exercise contains information on various features related to academic performance.
The goal is to build a multiple linear regression model to predict the performance index based on these features and evaluate the model's performance.

**Dataset**
The dataset consists of the following features:

Hours Studied: Number of hours spent studying.
Previous Scores: Scores from previous exams.
Extracurricular Activities: Whether extracurricular activities were participated in (Yes or No).
Sleep Hours: Number of hours of sleep.
Sample Question Papers Practiced: Number of sample question papers practiced.
Performance Index: The target variable, representing the performance index.

        Hours Studied  Previous Scores Extracurricular Activities  Sleep Hours  Sample Question Papers Practiced  Performance Index
0              7               99                        Yes            9                                1               91.0
1              4               82                         No            4                                2               65.0
2              8               51                        Yes            7                                2               45.0
3              5               52                        Yes            5                                2               36.0
4              7               75                         No            8                                5               66.0


# Approach
**Dataset Preparation**:
Loaded and preprocessed the dataset to handle features and target variable.
Encoded categorical variables where necessary.

**Model Training**:
Split the dataset into training and testing sets.
Trained a multiple linear regression model using the Hours Studied, Previous Scores, Extracurricular Activities, Sleep Hours, and Sample Question Papers Practiced features to predict Performance Index.
Saved the trained model using joblib.

**Prediction Function**:
Created a function to make predictions using the trained model. This function takes input values for each feature and outputs the predicted performance index.

**Evaluation**:
Evaluated the model using metrics such as Mean Squared Error (MSE) and R² Score to assess its performance.
The model achieved an `MSE of 4.08` and an `R² score of 0.99`, indicating very good performance with low prediction error and a high proportion of variance explained by the model
