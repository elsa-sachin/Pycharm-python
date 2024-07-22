"""Write a python program that takes 3 numbers as input from the user and the
prints out the sum of those numbers"""

num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number :"))

print(num1,"+",num2,"+",num3,"=",num1+num2+num3)



num=int(input("Enter the number:"))
sum=0
num1=num
while (num!=0) :
    temp=num%10
    sum+=temp
    num=num//10

print("Sum of ",num1 ,"=",sum)