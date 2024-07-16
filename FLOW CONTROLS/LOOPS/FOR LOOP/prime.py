#check given no.is prime or not

num=int(input("Enter the number:"))
flag = 0
for i in range(2,num):
    if(num%i==0):
        flag=1


if flag==1 :
    print("Not Prime Number")
else:
    print("Prime Number")
