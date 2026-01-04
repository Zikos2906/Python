gesture = input("Show gesture (Shaka/Wai/Peace): ").capitalize()

if gesture == "Shaka":
    print("Costume: Hawaii/Polynesian - Background: Beach")
elif gesture == "Wai":
    print("Costume: Thailand - Background: Temple")
elif gesture == "Peace":
    print("Costume: USA/Western - Background: City")
else:
    print("Unknown gesture.")