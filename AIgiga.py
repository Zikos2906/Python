words = input("Talk to GIGA: ").lower()

if "hello" in words or "hi" in words:
    print("GIGA: Hello friend! Let's play.")
elif "game" in words:
    print("GIGA: I love games! Which one?")
else:
    print("GIGA: That sounds interesting!")