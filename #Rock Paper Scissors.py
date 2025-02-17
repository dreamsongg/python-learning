#Rock Paper Scissors

import random

player_choice = int(input("Type 1 for rock, 2 for paper, and 3 for scissors\n"))



RPS = ["rock", "paper", "scissors"]


RPS = random.randint(0,3) - 1

if player_choice == 1:
    if RPS == 1:
        print("You have tied")
    elif RPS == 2: 
        print("You have lost! Paper covers rock")
    else:
        print("You have won! Rock crushes scissors")
if player_choice == 2:
    if RPS == 1:
        print("You have won the game, paper covers rock")
    elif RPS == 2:
        print("You have tied")
    else:
        print("You have lost the game, scissors cut paper")
if player_choice == 3:
    if RPS == 1:
        print("You have lost the game, rock crushes scissors")
    elif RPS == 2:
        print("You hve won the game, scissors cuts paper")
    else:
        print("You have tied")