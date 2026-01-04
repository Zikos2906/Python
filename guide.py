location = "Start"
command = input("Where to? (museum/park): ").lower()

if command == "museum":
    location = "Museum"
    print("Navigating to the Museum...")
elif command == "park":
    location = "Park"
    print("Navigating to the Park...")
else:
    print("Command not recognized.")

print("Current location:", location)