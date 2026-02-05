import random 
class fruitquiz :
    def __init__(self):
        self.fruits = {"apple" : "red", "banana" : "yellow" , "orange" : "orange"}
    def quiz(self):
        while True :
            fruit,color = random.choice(list(self.fruits.items()))
            print("What is the color of : ",fruit)
            answer = input()
            if answer == color :
                print("correct answer")
            else:
                print("wrong answer")
            choice = int(input("Enter 0 if u want to play again"))
            if choice :
             
             break
print("Welcome to fruit quiz")
obj = fruitquiz()
obj.quiz()