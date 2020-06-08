##SAIF IQBAL 1628421

currentMonth = input("Please enter the current month in digits:")
CurrentDate = input("Please enter the current date (7,9,13, etc.):")
CurrentYear = input("Please enter the current year:")

BirthMonth = input("Please enter your birth month in digits:")
BirthDate= input("Please enter your birth date:")
BirthYear= input("Please enter your birth year:")



age=CurrentYear-BirthYear

if BirthMonth == currentMonth:
    if CurrentDate == BirthDate:
        print("Happy Birthday")
print"Your are %s" %age

