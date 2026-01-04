import random

options = ["Rock", "Paper", "Scissors"]
cpu_choice = random.choice(options)
user_gesture = input("Show your gesture: ").capitalize()

print("Computer chose:", cpu_choice)

if user_gesture == cpu_choice:
    print("It's a tie!")
elif (user_gesture == "Rock" and cpu_choice == "Scissors") or \
     (user_gesture == "Paper" and cpu_choice == "Rock") or \
     (user_gesture == "Scissors" and cpu_choice == "Paper"):
    print("You win!")
else:
    print("Computer wins!")