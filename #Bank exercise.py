#Bank exercise

import random

names_string = input("Type in every name within the group.\n")

names = names_string.split(",")

random_index = random.randint(0, len(names) - 1)

random_name = names[random_index]

print(random_name)

