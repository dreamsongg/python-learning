#fizzbuzz exercise



for i in range(1, 101):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result = result + "Buzz"
    print(result)






#for number in range(1, 101):
    #if number % 3 == 0 and number % 5 == 0:
        #print("FizzBuzz")
    #elif number % 3 == 0:
        #print("Fizz")
    #elif number % 5 == 0:
       #print("Buzz")