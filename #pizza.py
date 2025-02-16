#pizza

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L?\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("DO you want extra cheese? Y or N\n")


bill = 0


if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25

if size == "S" and add_pepperoni == "Y":
    bill = bill + 2
elif size == "M" or size == "L" and add_pepperoni =="Y":
    bill = bill + 3
if extra_cheese == "Y":
    bill = bill + 1
print(f"Your final bill is: {bill}")