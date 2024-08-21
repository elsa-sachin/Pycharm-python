num=int(input("Enter a number: "))
num1=num
c=0
sum=0
def count(num1):
    c=0
    while(num1>0):
        num1=num1//10
        c+=1
    return c


while(num1>0):
    temp=num1%10
    sum=sum+(temp**count(num))
    num1=num1//10

if num==sum:
    print(f"{num} is arm")
else:

    print(f"{num} not arm")