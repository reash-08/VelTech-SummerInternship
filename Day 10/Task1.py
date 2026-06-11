import joblib
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

model = joblib.load(os.path.join(BASE_DIR, "final_model.pkl"))
encoders = joblib.load(os.path.join(BASE_DIR, "encoders.pkl"))
target_encoder = joblib.load(os.path.join(BASE_DIR, "target_encoder.pkl"))

print("Model Loaded Successfully")
print()

print("Features Used:")
print(model.feature_names_in_)

print()

print("Encoder Keys:")
print(encoders.keys())

print()

print("Target Classes:")
print(target_encoder.classes_)