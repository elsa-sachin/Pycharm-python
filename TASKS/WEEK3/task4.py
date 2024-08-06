""""Python program to check if a given number is an Armstrong number"""

def count(num1):
    c=0
    while(num1!=0):
        t=num1%10
        num1=num1//10
        c += 1
    return c


num=int(input("Enter a number :"))
num1=num
count1=count(num1)
sum=0
while(num1!=0):
    temp=num1%10
    sum=sum+pow(temp,count1)
    num1=num1//10

if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong")
