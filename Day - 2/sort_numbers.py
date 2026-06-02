odd_numbers = []
even_numbers = []
for i in range(10):
    n = int(input("Enter a number: "))
    if (n%2==0):
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)