# try:
#    number = int(input("Enter The number : "))
#    print("The Number entered is : " , number)

# except ValueError as ex :
#     print("Exception",ex)

try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 4,5")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")
