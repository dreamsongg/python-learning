#treasure map
import random

row1 = ["☐", "☐", "☐"]
row2 = ["☐", "☐", "☐"]
row3 = ["☐", "☐", "☐"]

map = [row1, row2, row3]
print(f"{row1}\n{row3}\n{row3}\n")

position = input("Where would you like to hide the treasure?\n")


position = treasure_placement.choice(map)

print(treasure_placement)