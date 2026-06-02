def get_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 75:
        return "B"
    elif grade >= 60:
        return "C"
    elif grade >= 45:
        return "D"
    else:
        return "F"


for i in range(5):
    try:
        grade = int(input("Enter a mark: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    letter_grade = get_grade(grade)
    print(f"The letter grade for {grade} is {letter_grade}.")