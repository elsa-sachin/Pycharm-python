lower = int(input("Enter the lower limit :"))
upper = int(input("Enter the upper limit :"))
sum1 = 0
sum2 = 0
while(lower <= upper):
    if(lower %2 == 0):
        sum1 += lower
    else:
        sum2 += lower
    lower += 1
print("Sum of even numbers :",sum1)
print("Sum of odd numbers :",sum2)