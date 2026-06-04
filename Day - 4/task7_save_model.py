import os
import pickle
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")
model_file = os.path.join(script_dir, "accident_severity_model.pkl")
predictions_file = os.path.join(script_dir, "task7_predictions.csv")

print("=" * 70)
print("TASK 7 - SAVE AND LOAD MODEL")
print("=" * 70)

# ==================================================
# 1. read_csv()
# ==================================================

df = pd.read_csv(csv_path)

# ==================================================
# 2. shape
# ==================================================

print("\nDataset Shape:")
print(df.shape)

# ==================================================
# 3. columns
# ==================================================

print("\nColumns:")
print(df.columns.tolist())

# ==================================================
# 4. head()
# ==================================================

print("\nFirst 5 Records:")
print(df.head())

# ==================================================
# 5. tail()
# ==================================================

print("\nLast 5 Records:")
print(df.tail())

# ==================================================
# 6. info()
# ==================================================

print("\nDataset Info:")
df.info()

# ==================================================
# 7. describe()
# ==================================================

print("\nStatistics:")
print(df.describe())

# ==================================================
# 8. isnull()
# ==================================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==================================================
# 9. fillna()
# ==================================================

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        numeric_col = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(numeric_col.median())

# ==================================================
# 10. value_counts()
# ==================================================

print("\nSeverity Distribution:")
print(df["Accident_Severity"].value_counts())

# ==================================================
# 11. nunique()
# ==================================================

print("\nUnique Values:")
print(df.nunique())

# ==================================================
# 12. groupby()
# ==================================================

print("\nAverage Casualties by Severity:")
print(
    df.groupby("Accident_Severity")
      ["Number_of_Casualties"]
      .mean()
)

# ==================================================
# 13. copy()
# ==================================================

data = df.copy()

# ==================================================
# 14. select_dtypes()
# ==================================================

cat_cols = data.select_dtypes(
    include="object"
).columns

# ==================================================
# Label Encoding
# ==================================================

encoders = {}

for col in cat_cols:

    le = LabelEncoder()

    data[col] = le.fit_transform(
        data[col].astype(str)
    )

    encoders[col] = le

# ==================================================
# 15. corr()
# ==================================================

numeric = data.select_dtypes(
    include=np.number
)

print("\nCorrelation Matrix:")
print(
    numeric.corr().round(2)
)

# ==================================================
# Features
# ==================================================

features = [

    "Road_Type",

    "Weather_Conditions",

    "Light_Conditions",

    "Speed_limit",

    "Number_of_Vehicles",

    "Number_of_Casualties",

    "Urban_or_Rural_Area",

    "Day_of_Week"

]

target = "Accident_Severity"

X = data[features]

y = data[target]

# ==================================================
# Train-Test Split
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)

# ==================================================
# Train Model
# ==================================================

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42
)

model.fit(X_train, y_train)

# ==================================================
# Accuracy
# ==================================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nModel Accuracy: {accuracy:.4f}")

# ==================================================
# Save Model
# ==================================================

with open(model_file, "wb") as file:
    pickle.dump(model, file)

print(f"\nModel Saved: {model_file}")

# ==================================================
# Load Model
# ==================================================

with open(model_file, "rb") as file:

    loaded_model = pickle.load(file)

print("Model Loaded Successfully")

# ==================================================
# Predict Using Loaded Model
# ==================================================

sample_data = X_test.head(10)

loaded_predictions = loaded_model.predict(
    sample_data
)

# ==================================================
# 16. DataFrame()
# ==================================================

results = pd.DataFrame({

    "Actual": y_test.head(10).values,

    "Predicted": loaded_predictions

})

# ==================================================
# 17. sort_values()
# ==================================================

results = results.sort_values(
    by="Actual"
)

print("\nPrediction Results:")
print(results)

# ==================================================
# 18. sample()
# ==================================================

print("\nRandom Prediction Samples:")
print(results.sample(5))

# ==================================================
# 19. astype()
# ==================================================

results["Actual"] = (
    results["Actual"]
    .astype(int)
)

results["Predicted"] = (
    results["Predicted"]
    .astype(int)
)

# ==================================================
# 20. to_csv()
# ==================================================

results.to_csv(
    predictions_file,
    index=False
)

print("\nPredictions Saved:")
print(predictions_file)

# ==================================================
# Model File Size
# ==================================================

size = os.path.getsize(
    model_file
)

print(f"\nModel Size: {size/1024:.2f} KB")

print("\nTASK 7 COMPLETED SUCCESSFULLY")