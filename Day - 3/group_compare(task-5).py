import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "student-mat.csv"

df = pd.read_csv(csv_path, sep="\t")

avg_g3_by_study_time = df.groupby("studytime")["G3"].mean()
avg_g3_by_sex = df.groupby("sex")["G3"].mean()
top_5_students = df.nlargest(5, "G3")[["school", "sex", "age", "studytime", "G3"]]

print("Student dataset summary using student-mat.csv")
print("--------------------------------------------")
print("Average G3 grade by study time (1=less, 4=more):")
for study_time, avg_grade in avg_g3_by_study_time.items():
    print(f"  studytime={study_time}: {avg_grade:.2f}")

print("\nAverage G3 grade by sex:")
for sex, avg_grade in avg_g3_by_sex.items():
    print(f"  {sex}: {avg_grade:.2f}")

print("\nTop 5 students by G3 grade:")
for index, row in top_5_students.iterrows():
    print(f"  {row['school']} | sex={row['sex']} | age={row['age']} | studytime={row['studytime']} | G3={row['G3']}")
