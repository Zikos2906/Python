import random

fruits = ["Apple", "Banana", "Grapes", "Orange"]
score = 0

target = random.choice(fruits)
print("Recognize this fruit:", target)

guess = input("What fruit is detected? ")

if guess.lower() == target.lower():
    score += 1
    print("Correct! Score:", score)
else:
    print("Wrong fruit")