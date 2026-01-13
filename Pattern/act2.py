rows=int(input("how many rows do you want?"))
num=1
for row in range (1,rows+1):
    for i in range(1,row+1):
     print(num,end=" ")
     num+=1
    print() 
