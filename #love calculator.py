#love calculator

print("Welcome to the love calculator")
name1 = input("What is your name\n")
name2 = input("What is their name?\n")

combined_names = (name1 + name2).upper()


t_count = combined_names.count("T")
r_count = combined_names.count("R")
u_count = combined_names.count("U")
e_count = combined_names.count("E")

true_count = t_count + r_count + u_count + e_count

l_count = combined_names.count("L")
o_count = combined_names.count("O")
v_count = combined_names.count("V")
e_count = combined_names.count("E")

love_count = l_count + o_count + v_count + e_count


score = str(true_count) + str(love_count)

score = int(score)



if score < 10 or score > 90:
    print(f"Your score is {score}. You go together like coke and mentos")
elif score >= 40 or score <= 50:
    print(f"Your score is {score}. you are alright together")
else:
    print(f"Your score is {score}")

