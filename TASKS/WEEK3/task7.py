"""Write a program to accept a number and check whether its a perfect number or not.


Perfect  number is a number which is equal to the sum of its divisors.


For ex: 6 , its divisors are 1,2,3. So sum of divisors 1+2+3 is also 6
"""
num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
    if (num%i==0):
        sum+=i
if num==sum:
    print("Perfect number")
else:
    print("Not a perfect number")
