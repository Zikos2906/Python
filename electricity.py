unit = float(input("How many units did you consume last month: "))
if unit<=50:
    cost = 2.60
    tax = 25
    total_bill = unit*cost+tax
    print("Your total Bill is ",total_bill)
elif unit>50 and unit<=200:
    cost = 5.26
    tax = 75
    total_bill = unit*cost+tax
    print("Your total bil is : ",total_bill)
elif unit>200:
    cost =8.45
    tax = 75
    total_bill = unit*cost+tax
    print("Your Total bill is: ",total_bill)
else:
    print("Invalid Entry")