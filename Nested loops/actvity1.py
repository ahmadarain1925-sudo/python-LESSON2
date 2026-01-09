word=input("enter the word:")
char=input("enter an alphabet that you are searching in the word:")
count=0
for i in word:
    if i==char:
        count+=1
print("the letter",char,"appears",count,"times")