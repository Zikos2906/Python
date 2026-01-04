moods = {1: "😢", 2: "🙁", 3: "😐", 4: "🙂", 5: "😁"}

level = int(input("Slide (1-5): "))

if level in moods:
    print(moods[level])
else:
    print("Out of range")