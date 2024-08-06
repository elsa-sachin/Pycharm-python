"""Python program to display all numbers within a range except the prime numbers."""

low=int(input("Enter lower limit :"))
upper=int(input("Enter upper limit :"))

for i in range(low,upper+1):
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
    if f==1:
        print(i)


