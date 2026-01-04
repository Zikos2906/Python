score = 0

print("Quiz Time")

answer = input("What is 2 + 2? ")
if answer == "4":
    score += 1

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    score += 1

print("Your score is", score)