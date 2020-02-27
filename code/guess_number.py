import random
 
target = random.randint(1,100)
count = 0

print("Please guess the number between 1 and 100?")

while True:
    number = int(input())
    if number <= 0 or number > 100:
        print("Error! number must be between in 1 and 100!")
    elif number < target:
        print("shoud be bigger, once again")
    elif number > target:
        print("shoud be smaller, once again")
    else:
        print("Wow, greate! That is ", target)
        break
    count = count + 1

print("You guessed", count + 1, "times!")
