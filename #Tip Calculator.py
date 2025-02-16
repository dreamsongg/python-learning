#Tip Calculator
print("Welcome to the tip calculator")

bill = input("What was the total bill?\n")

tip = input("What percentage tip would you like to give?\n")

split = input("How many people to split the bill\n")

tip = float(tip)
bill = float(bill)
split = int(split)


tip_amount = (tip / 100) * bill
totalPrice = bill + tip_amount
shouldPay =  totalPrice / split 

print(f'Each person should pay: ${shouldPay:.2f}') 








