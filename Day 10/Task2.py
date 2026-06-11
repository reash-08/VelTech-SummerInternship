import sys
from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Load files once
model = joblib.load(BASE_DIR / "final_model.pkl")
encoders = joblib.load(BASE_DIR / "encoders.pkl")
target_encoder = joblib.load(BASE_DIR / "target_encoder.pkl")


def predict(inputs: dict) -> dict:

    try:

        # Convert input to DataFrame
        input_df = pd.DataFrame([inputs])

        # Encode ONLY categorical columns
        categorical_cols = [
            "Road_Type",
            "Weather_Conditions",
            "Road_Surface_Conditions",
            "Light_Conditions",
            "Urban_or_Rural_Area"
        ]

        for col in categorical_cols:

            input_df[col] = (
                encoders[col]
                .transform(
                    input_df[col].astype(str)
                )
            )

        # Prediction
        prediction = model.predict(input_df)[0]

        # Confidence
        probabilities = model.predict_proba(input_df)[0]

        predicted_label = (
            target_encoder
            .inverse_transform([prediction])[0]
        )

        confidence = (
            max(probabilities) * 100
        )

        return {

            "prediction":
            predicted_label,

            "confidence":
            f"{confidence:.2f}%"

        }

    except Exception as e:

        return {

            "prediction":
            "Error",

            "confidence":
            "N/A",

            "error":
            str(e)

        }


# Test Sample
sample = {

    "Road_Type":
    "Single carriageway",

    "Weather_Conditions":
    "Fine no high winds",

    "Road_Surface_Conditions":
    "Dry",

    "Light_Conditions":
    "Daylight",

    "Speed_limit":
    30,

    "Urban_or_Rural_Area":
    "Urban",

    "Number_of_Vehicles":
    2,

    "Number_of_Casualties":
    1

}

print(predict(sample))