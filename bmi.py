print("Let's Calculate your BMI")
weight = int(input("Enter your weight in KG"))
height = float(input("Enter you height in meters"))

bmi = weight/ (height*height)
bmi = float(bmi)
print("Your BMI is",bmi)

if bmi < 16 :
    print("severe thinness")
elif bmi > 16 and bmi < 17:
    print("Moderate Thinness")
elif bmi > 17 and bmi < 18.5:
    print("Mild Thinness")
elif bmi > 18.5 and bmi < 25:
    print("Normal")
elif bmi < 25:
    print("Overweight")
else :
    print("EAT HEALTHY")
