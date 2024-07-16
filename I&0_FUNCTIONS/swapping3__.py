""" Single line swapping"""

a,b,c,d=10,20,30,40
# above declaration is same as below declration
a=10
b=20
c=30
d=40

num1=10
num2=20
print("Before swapping")
print("Number1 is",num1)
print("Number2 is",num2)

num1,num2=num2,num1   #single line swapping
print("After swapping")
print("Number1 is",num1)
print("Number2 is",num2)