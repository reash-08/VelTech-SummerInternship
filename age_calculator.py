birth_yr = int(input("Enter your birth year : "))
if birth_yr > 2026 :
    print("Error : Invalid birth year")
else : 
    age = 2026 - birth_yr
    age_aft_10_yrs = age +10
print(f"Your age is {age} years.")
print(f"Your age after 10 years is {age_aft_10_yrs} years.")