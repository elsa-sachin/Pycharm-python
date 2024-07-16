lower=int(input("Enter the lower limit :"))
upper=int(input("Enter the upper limit :"))

sum1=0
sum2=0

for i in range(lower,upper+1):
    if(i%2==0):
        sum1+=i
    else:
        sum2+=i
print("Sum of even numbers:",sum1)
print("Sum of odd numbers:",sum2)
