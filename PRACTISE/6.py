lower=int(input("Enter a lower limit:"))
upper=int(input("Enter a upper limit:"))


for i in range(lower,upper+1):
    f=0
    for j in range(2,i):
        if i%j == 0:
            f=1
        else:
            break
    if f ==0:
        print(i)