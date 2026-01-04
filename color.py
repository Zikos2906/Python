colors = ["purple", "blue", "pink"]
detected = input("What color do you see? (purple/blue/pink): ").lower()

if detected in colors:
    print("Butterfly Costume: " + detected.capitalize())
else:
    print("Butterfly Costume: Normal")