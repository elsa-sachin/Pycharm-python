""" Count the total number of digits in a number"""



def count(num1):
    c=0
    while(num1!=0):
        t=num1%10
        num1=num1//10
        c += 1
    return c

num=int(input("Enter the number "))
print(count(num))