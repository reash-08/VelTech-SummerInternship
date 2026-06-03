import numpy as np

marks = np.array([280, 245, 300, 270, 230, 255, 295, 260, 220, 275])

mean_score = marks.mean()
highest_score = marks.max()
lowest_score = marks.min()
std_dev = marks.std()
passed_count = np.count_nonzero(marks >= 250)

print("Student Marks Summary Report")
print("-----------------------------")
print(f"Marks: {marks}")
print(f"Mean score: {mean_score:.2f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Standard deviation: {std_dev:.2f}")
print(f"Number of students passed (>= 250): {passed_count}")
