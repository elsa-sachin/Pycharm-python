"""Write a program to check whether given year is leap year or not"""

yr=int(input("Enter the year:"))

if yr % 4==0 or yr %400 ==0 and yr % 100==0:
    print(f"{yr} is a leap year")
else:
    print(f"{yr} not a leap year")