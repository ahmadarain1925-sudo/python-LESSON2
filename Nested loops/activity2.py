upper_limit=int(input("enter the upper limi:"))
lower_limit=int(input("enter the lower limit"))
for j in range (lower_limit,upper_limit+1):
  for i in range (2,j):
    if j%i==0:
      break
  else:
    print(j)