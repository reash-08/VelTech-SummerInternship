# VelTech-SummerInternship 
My project and it's source code

# Day 4 - Road Accident Severity Prediction

## Overview

This project focuses on predicting road accident severity using machine learning techniques. The dataset used is **accident_50k.csv**, which contains 50,000 accident records and 34 features related to road conditions, weather, vehicles, casualties, and accident severity.

## Objectives

* Analyze road accident data.
* Perform data preprocessing and exploratory data analysis (EDA).
* Create multiple visualizations to understand accident patterns.
* Build a machine learning model to predict accident severity.
* Evaluate model performance using classification metrics.
* Save and reuse the trained model.

## Dataset Information

* Dataset Name: accident_50k.csv
* Total Records: 50,000
* Total Features: 34
* Target Variable: Accident_Severity

### Selected Features

* Road_Type
* Weather_Conditions
* Speed_limit
* Number_of_Vehicles

### Target

* Accident_Severity

  * Slight
  * Serious
  * Fatal

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Pickle
* Git & Git LFS

## Project Tasks

### Task 1 - Data Visualization

Created 15+ visualizations including:

* Bar Chart
* Pie Chart
* Histogram
* Line Chart
* Scatter Plot
* Box Plot
* Violin Plot
* Heatmap
* Count Plot
* KDE Plot
* Area Chart
* Hexbin Plot
* Strip Plot
* Swarm Plot
* ECDF Plot

### Task 2 - Dashboard Creation

Developed a dashboard containing:

* Severity Distribution
* Monthly Accident Trend
* Speed Limit Analysis
* Average Casualties by Road Type

### Task 3 - Train-Test Split Analysis

Compared multiple train-test split ratios:

* 10%
* 20%
* 30%
* 40%

Evaluated performance using Accuracy Score and F1 Score.

### Task 4 - Accident Severity Prediction

Built a Random Forest Classification model to predict accident severity using selected accident-related features.

### Task 5 - Feature Comparison

Compared different features to determine their impact on accident severity prediction.

### Task 6 - Prediction Analysis

Performed model evaluation using:

* Accuracy Score
* Classification Report
* Confusion Matrix
* Feature Importance Analysis

### Task 7 - Model Saving and Loading

Saved the trained model using Pickle:

* accident_severity_model.pkl

Loaded the saved model and performed predictions successfully.

## Results

* Successfully completed data preprocessing and feature engineering.
* Generated multiple visualizations for accident analysis.
* Built and evaluated a Random Forest Classifier.
* Identified important factors influencing accident severity.
* Saved the trained model for future use.

## Learning Outcomes

Through this project, I learned:

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Data Visualization Techniques
* Feature Engineering
* Classification Models
* Model Evaluation
* Model Serialization using Pickle
* GitHub and Git LFS for large files

## Future Improvements

* Hyperparameter Tuning
* XGBoost and LightGBM Models
* Real-Time Prediction System
* Interactive Dashboard Development
* Web Application Deployment

