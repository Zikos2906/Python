import random 

def welcome ():
    print("Welcome to Number Guessing Game !")

def generate():
    number = random.randint(1,10)
    return number

computer = generate()
welcome()
chances = 3

while True:
    print("You have",chances,"chances left")
    mynum = int(input("Enter any number from 1-10"))
    if(computer == mynum):
        print("You have guessed the number !")
        break
    else:
        if(mynum>computer):
            print("Try a lesser number.")
        else:
            print("Try a higher number")
        chances = chances-1
        print("Try again")
    
    if(chances == 0):
        print("No more chances left")
        print("Computer Number is ",computer)
        break
