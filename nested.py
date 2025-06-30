medical = input("Do you Have any Medical issues? (y/n): ")
if medical == "y":
    print("You are eligible for the Exam!")
else:
    attn = float(input("Enter your Attendance percentage: "))
    if attn >=75:
        print("you are eligible for the exam!")
    else:
        print("you are not eligible fo the exam...!")