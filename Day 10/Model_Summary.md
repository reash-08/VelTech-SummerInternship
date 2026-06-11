# Model Summary Card

## Project

Road Accident Severity Prediction System

## Algorithm

Gradient Boosting Classifier (Tuned using GridSearchCV)

## Dataset

UK Road Accident Dataset (accident_50k.csv)

* Total Records: 50,000
* Target Variable: Accident Severity
* Classes: Fatal, Serious, Slight

## Final Performance

| Metric                 | Score        |
| ---------------------- | ------------ |
| F1-Score (Weighted)    | 0.780        |
| Cross Validation Score | 0.780 ± 0.02 |

## Input Features

| Feature                 | Type        | Example            |
| ----------------------- | ----------- | ------------------ |
| Road_Type               | Categorical | Single carriageway |
| Weather_Conditions      | Categorical | Fine no high winds |
| Road_Surface_Conditions | Categorical | Dry                |
| Light_Conditions        | Categorical | Daylight           |
| Speed_limit             | Numeric     | 30                 |
| Urban_or_Rural_Area     | Categorical | Urban              |
| Number_of_Vehicles      | Numeric     | 2                  |
| Number_of_Casualties    | Numeric     | 1                  |

## Required Files

| File               | Purpose                                 |
| ------------------ | --------------------------------------- |
| final_model.pkl    | Final tuned Gradient Boosting model     |
| encoders.pkl       | Label encoders for categorical features |
| target_encoder.pkl | Encoder for accident severity labels    |

## Sample Input

{
"Road_Type": "Single carriageway",
"Weather_Conditions": "Fine no high winds",
"Road_Surface_Conditions": "Dry",
"Light_Conditions": "Daylight",
"Speed_limit": 30,
"Urban_or_Rural_Area": "Urban",
"Number_of_Vehicles": 2,
"Number_of_Casualties": 1
}

## Sample Output

{
"prediction": "Slight",
"confidence": "89.48%"
}

## How to Use

1. Load `final_model.pkl`
2. Load `encoders.pkl`
3. Load `target_encoder.pkl`
4. Pass input data to the `predict()` function
5. Receive accident severity prediction and confidence score

## Handoff Checklist

Files required by Flask Developer:

* final_model.pkl
* encoders.pkl
* target_encoder.pkl
* predict_function.py

Prediction Flow:

User Input → Encoding → Model Prediction → Severity Label → Confidence Score

Expected Output:

{
"prediction": "Fatal / Serious / Slight",
"confidence": "XX.XX%"
}
