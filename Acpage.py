try:
    age = int(input())

    if age < 0:
        print("Invalid age")
    else:
        if age % 2 == 0:
            print("Even age")
        else:
            print("Odd age")

except ValueError:
    print("Invalid input")






