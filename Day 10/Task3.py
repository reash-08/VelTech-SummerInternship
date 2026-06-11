import sys
from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
for path in (SCRIPT_DIR, BASE_DIR):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from Task2 import predict

test_cases = [

    # Case 1 - Normal Urban Accident
    {
        "Road_Type": "Single carriageway",
        "Weather_Conditions": "Fine no high winds",
        "Road_Surface_Conditions": "Dry",
        "Light_Conditions": "Daylight",
        "Speed_limit": 30,
        "Urban_or_Rural_Area": "Urban",
        "Number_of_Vehicles": 2,
        "Number_of_Casualties": 1
    },

    # Case 2 - Normal Urban Accident
    {
        "Road_Type": "Roundabout",
        "Weather_Conditions": "Fine no high winds",
        "Road_Surface_Conditions": "Dry",
        "Light_Conditions": "Daylight",
        "Speed_limit": 40,
        "Urban_or_Rural_Area": "Urban",
        "Number_of_Vehicles": 2,
        "Number_of_Casualties": 1
    },

    # Case 3 - Average Conditions
    {
        "Road_Type": "Dual carriageway",
        "Weather_Conditions": "Fine no high winds",
        "Road_Surface_Conditions": "Dry",
        "Light_Conditions": "Daylight",
        "Speed_limit": 50,
        "Urban_or_Rural_Area": "Urban",
        "Number_of_Vehicles": 2,
        "Number_of_Casualties": 1
    },

    # Case 4 - High Risk
    {
        "Road_Type": "Single carriageway",
        "Weather_Conditions": "Fog or mist",
        "Road_Surface_Conditions": "Wet or damp",
        "Light_Conditions": "Darkness - no lighting",
        "Speed_limit": 70,
        "Urban_or_Rural_Area": "Rural",
        "Number_of_Vehicles": 3,
        "Number_of_Casualties": 2
    },

    # Case 5 - Extreme Risk
    {
        "Road_Type": "Slip road",
        "Weather_Conditions": "Snowing no high winds",
        "Road_Surface_Conditions": "Snow",
        "Light_Conditions": "Darkness - no lighting",
        "Speed_limit": 70,
        "Urban_or_Rural_Area": "Rural",
        "Number_of_Vehicles": 4,
        "Number_of_Casualties": 3
    },

    # Case 6 - Edge Minimum Values
    {
        "Road_Type": "Single carriageway",
        "Weather_Conditions": "Fine no high winds",
        "Road_Surface_Conditions": "Dry",
        "Light_Conditions": "Daylight",
        "Speed_limit": 20,
        "Urban_or_Rural_Area": "Urban",
        "Number_of_Vehicles": 1,
        "Number_of_Casualties": 1
    },

    # Case 7 - Edge Maximum Values
    {
        "Road_Type": "Dual carriageway",
        "Weather_Conditions": "Raining + high winds",
        "Road_Surface_Conditions": "Flood over 3cm deep",
        "Light_Conditions": "Darkness - no lighting",
        "Speed_limit": 70,
        "Urban_or_Rural_Area": "Rural",
        "Number_of_Vehicles": 10,
        "Number_of_Casualties": 10
    },

    # Case 8 - Known Test Style
    {
        "Road_Type": "Single carriageway",
        "Weather_Conditions": "Fine no high winds",
        "Road_Surface_Conditions": "Dry",
        "Light_Conditions": "Darkness - lights lit",
        "Speed_limit": 30,
        "Urban_or_Rural_Area": "Urban",
        "Number_of_Vehicles": 2,
        "Number_of_Casualties": 1
    },

    # Case 9 - Known Test Style
    {
        "Road_Type": "Single carriageway",
        "Weather_Conditions": "Raining no high winds",
        "Road_Surface_Conditions": "Wet or damp",
        "Light_Conditions": "Darkness - lights lit",
        "Speed_limit": 60,
        "Urban_or_Rural_Area": "Rural",
        "Number_of_Vehicles": 3,
        "Number_of_Casualties": 2
    },

    # Case 10 - Invalid Input
    {
        "Road_Type": "Single carriageway",
        "Weather_Conditions": "Fine no high winds",
        "Road_Surface_Conditions": "Dry",
        "Light_Conditions": "Daylight",
        "Speed_limit": -10,
        "Urban_or_Rural_Area": "Urban",
        "Number_of_Vehicles": -1,
        "Number_of_Casualties": -1
    }
]

results = []

for i, case in enumerate(test_cases, start=1):

    result = predict(case)

    results.append({
        "Case": i,
        "Prediction": result.get("prediction"),
        "Confidence": result.get("confidence"),
        "Status": "PASS" if result.get("prediction") != "Error" else "ERROR"
    })

results_df = pd.DataFrame(results)

print("\nTEST RESULTS\n")
print(results_df.to_string(index=False))

results_df.to_csv(
    "test_results.csv",
    index=False
)

print("\nSaved as test_results.csv")