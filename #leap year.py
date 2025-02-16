#leap year

year = int(input("Which year do you want to check?\n"))\


if (year % 4 == 0) and year % 100 != 0 or year % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")