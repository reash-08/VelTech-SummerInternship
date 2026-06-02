pin = 4565
attempt = 0
while attempt < 3:
    try:
        user_input = int(input("Enter your 4-digit PIN: "))
    except ValueError:
        print("Please enter digits only.")
        continue

    if user_input == pin:
        print("Access granted.")
        break
    else:
        attempt += 1
        if attempt < 3:
            print("Incorrect PIN. Try again.")
        else:
            print("Too many incorrect attempts. Your card has been blocked.")