#treasure map
import random

row1 = ["☐", "☐", "☐"]
row2 = ["☐", "☐", "☐"]
row3 = ["☐", "☐", "☐"]

map = [row1, row2, row3]
print(f"{row1}\n{row3}\n{row3}\n")

position = input("Where would you like to hide the treasure?\n")



row_index = int(position[0]) - 1 
col_index = int(position[1]) - 1

if row_index > 2:
    row_index = 2
    print("This row is out of range")
if col_index > 2:
    col_index = 2
    print("This column is out of range")

map[row_index][col_index] = "x"


print(map)