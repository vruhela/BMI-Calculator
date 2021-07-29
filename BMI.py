print("Hello, I am a BMI Calculator and I am here to calculate you BMI. So let's get started.")
print()
weight=float((input("Enter your weight in Kg (example- 50.5):")))
height=float(input("Enter your height in Meters (example- 5.0):"))

bmi=weight/(height**2)
print("Your BMI is: ",round(bmi,2) )

if bmi<=18.5:
    print("You are UNDERWEIGHT!!")
elif bmi>18.5 and bmi<=24.9:
    print("You are NORMAL.")
elif bmi>24.9 and bmi<=29.9:
    print("You are OVERWEIGHT!!")
else:
    print("You are OBESE!!")             
