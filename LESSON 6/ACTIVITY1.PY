attendence=float(input("enter your attendace percentage"))
if attendence >75:
    print("you are allowed in exam")
else: 
   medical_cause =input("was it a medical cause?y/n")
   if medical_cause =="y":
    print("you are allowed in exam")
   else:
    print("you are not allowed to sit in exam")
