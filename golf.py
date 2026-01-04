import random

hole_dist = 10
power = int(input("Hit power (1-20): "))
swing_drift = random.randint(-2, 2)
total_hit = power + swing_drift

if total_hit == hole_dist:
    print("Hole in one!")
elif total_hit > hole_dist:
    print("Too hard")
else:
    print("Too short")