height = float(input("Enter your height in cms: "))
weight = float(input("Enter your weight in kgs: "))

# convert height from cm to meters
bmi = weight / (height /100)** 2



print("Your BMI is:", bmi)
if bmi <= 18.4:
    print("You are underweight")

elif bmi <= 24.9:
    print("You are healthy")

elif bmi <= 29.9:
    print("You are overweight")

elif bmi <=34.9:
    print("you are severly overweight")

elif bmi <=34.9:
    print("you are obese")

else :
    print ("you are severly obese")
    
