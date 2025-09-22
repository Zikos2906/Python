import random
Playing = True
computer = random.randint(0,9)

print("I will generate a number between 0-9 ")
print("To win the game the number must be the same")

while True:
    guess = int(input("Enter the Number: "))
    if guess == computer:
        print("Good Job You have Won!")
        break

    else:
        print("Try Again")





