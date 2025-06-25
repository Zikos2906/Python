char = input("Enter any character: ")
if len(char)!=1:
    print("Invalid")
else:
    if char.isalpha():
        print("It is a letter")
    else:
        print("it is not a letter")