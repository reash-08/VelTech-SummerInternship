for i in range(3):
    def generate_table(n):
        print(f"Multiplication Table for {n}:")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        print()
    try:
        number = int(input("Enter a number to generate its multiplication table: "))
        generate_table(number)
    except ValueError:
        print("Please enter a valid integer.")