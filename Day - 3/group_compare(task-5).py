import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "Accident_Information.csv"

df = pd.read_csv(csv_path)

# Average casualties by accident severity
avg_casualties_by_severity = df.groupby("Accident_Severity")["Number_of_Casualties"].mean()

# Average casualties by weather condition
avg_casualties_by_weather = df.groupby("Weather_Conditions")["Number_of_Casualties"].mean()

# Top 5 accidents with highest casualties
top_5_accidents = df.nlargest(
    5, "Number_of_Casualties"
)[[
    "Accident_Index",
    "Accident_Severity",
    "Number_of_Casualties",
    "Number_of_Vehicles",
    "Weather_Conditions",
    "Speed_limit"
]]

print("Accident Information Dataset Summary")
print("------------------------------------")

print("Average Number of Casualties by Accident Severity:")
for severity, avg_casualties in avg_casualties_by_severity.items():
    print(f"  Severity={severity}: {avg_casualties:.2f}")

print("\nAverage Number of Casualties by Weather Condition:")
for weather, avg_casualties in avg_casualties_by_weather.items():
    print(f"  Weather={weather}: {avg_casualties:.2f}")

print("\nTop 5 Accidents by Number of Casualties:")
for index, row in top_5_accidents.iterrows():
    print(
        f"  Accident_ID={row['Accident_Index']} | "
        f"Severity={row['Accident_Severity']} | "
        f"Casualties={row['Number_of_Casualties']} | "
        f"Vehicles={row['Number_of_Vehicles']} | "
        f"Weather={row['Weather_Conditions']} | "
        f"SpeedLimit={row['Speed_limit']}"
    )