#CYOA story

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

lakechoice = None
mansion = None

forkintheroad = input("You've found yourself at a fork in the roads, deep within the forest. Two pathways emerge, where would you like to go? Type left or right\n")


if forkintheroad == "right":
    lakechoice = input("You follow the path through the forest. The light shines radiantly through the trees as you approach a large lake. An old boat rests at the shoreline infront of you. Type swim or row to choose.\n")

if lakechoice == "row":
   mansion = input('''As you stare out into the eerily calm waters, you can see the movements of creatures just beneath the surface. Deciding not to risk it, you prepare the boat and embark.
    Moments pass, and as you slowly ride upon the calm waters of the lake, you spot a mansion hidden within the dense forest. After securing your trusty boat, you enter the mansion, and are presented with
    three doors, red blue and green. Type red, blue, or green to choose which door you'd like to enter.''')

if mansion == "red":
        print('''You step through the red door, entering a room lit with blue flame candles. Runes are drawn on the ground in a viscous, red liquid and each time you gaze at them
    they seem to morph. The harder you try to visualize the strange runic figures infront of you, the more difficult it becomes. Your vision blurs, and your head begins to hurt, feeling as though it is swelling.
    The last thoughts that flow from your now destroyed mind are that of fear, and the voices of otherwordly things. Game over''')
    
elif mansion == "blue":
        print('''You step through the blue door expecting another room, and instead you wake up laying in a bright, grassy field. A sense of calming and peace emerges from deep within your chest.
    Hours pass in blissful serenity, and you feel content to continue letting them pass. Days fly by as you sit in the beautiful field, a smile across your face as you watch the sky darken. Game over''')

elif mansion == "green":
    print('''You step through the green door, and continue throughout the mansion. Every step you get the feeling that somebody is watching you, but you continue on regardless.
    Hallways and rooms pass you by for what seems like an eternity, the mansion feeling far larger on the inside than it has any right to be. The end of the hallway nears.
    A golden door rests at the end, illuminating the area around it. The sight of the door feels you with fulfillment, as memories of your life grow more vivid. Pleasant feelings and contentedness fill you,
    and whatever regrets may have plagued you fade away as your spirit lightens. You step through the golden door, and what awaits you is the serene peace of a life well lived. You've returned home.
    You have won the game''')
    
elif forkintheroad == "left":
    print('''You've followed another path through the forest, and each step seemed to echo throughout the quiet and dense pine.
    The path darkens ahead of you, and the last thing you heard was your heartbeat. Your vision fades as figures dance all around you in the void. Game over''')
elif lakechoice == "swim":
        print('''You decide the boat is too damaged, and decide to swim. The further you swim ashore, the more your movements feel as though you are swimming in mud.
    The last thing you see is the sun over the lake, your last breath a pointless gasp. Game over''')

else:
    print("Invalid choice. Game over")
