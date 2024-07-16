#lower upper divisible by 5 sum


lower=int(input("Enter the lower limit:"))
upper=int(input("Enter the upper limit :"))

sum=0

while(lower<=upper):
    if(lower%5==0):
        sum +=lower
    lower+=1
print("Sum of numbers which are divisible by 5 :",sum)