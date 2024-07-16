"""break,continue,pass """


#break -to exit a loop

for i in range(1,51):
    if (i==25):
        break
    print(i)

#continue-it skips that condition and goes into the loop

for i in range(1,51):
    if (i==25):
        continue
    print(i)

#pass-do nothing
for i in range(1,51):
    if (i==25):
        pass
    print(i)

num=int(input("Enter a number:"))
if(num%2==0):
    print("Even number")
else:
    pass
