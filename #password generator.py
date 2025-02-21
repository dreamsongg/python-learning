#password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your passwword?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?"))


password = []

for randomletters in range(nr_letters):
    password.append(random.choice(letters))

for randomnumbers in range(nr_numbers):
    password.append(random.choice(numbers))

for randomsymbols in range(nr_symbols):
    password.append(random.choice(symbols))

user_password = ""

for items in password:
    user_password += items




print("Your password is: ", user_password)



