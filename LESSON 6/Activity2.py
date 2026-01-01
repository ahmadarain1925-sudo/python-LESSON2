#program to calculate eelectrycity bill
units=float(input("enter the unit consumed"))
if units <50:
    cost=units*2.6
    tax=25
elif units>=50 and units <100:
    cost=units*3.25
    tax=35
elif units>=100 and units <200:
    cost=units*5.26
    tax=45
else:
    cost=units*8.45
    tax=75
totalbill=cost+tax
print("total electrycity bill is",totalbill)
