#bmi calc 2.0

height = float(input("Please enter your height in m:\n"))
weight = float(input("Please enter your weight in kg\n"))


userheight = height ** 2
bmi = weight / userheight

if bmi <= 18.5:
    print(f"Your BMI is: {round(bmi)}. You are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is: {round(bmi)} You are normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is: {round(bmi)}. You are overweight")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {round(bmi)} You are obese.")
elif bmi > 35:
    print(f"Your BMI is {round(bmi)} You are clinically obese")










#print((round(bmi)))

