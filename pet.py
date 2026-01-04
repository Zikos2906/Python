boredom = 7
sleepiness = 3

if boredom > 5:
    action = input("Pet is bored. Play with toys? (y/n): ")
    if action == "y":
        boredom = 0
        print("Pet is happy now")

if sleepiness > 5:
    print("Pet is closing eyes. Sleeping...")
else:
    print("Pet is awake and alert")