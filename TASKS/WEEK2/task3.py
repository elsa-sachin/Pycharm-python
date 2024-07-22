"""Write a program to find greatest number among three numbers"""
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

if num1>num2 and num1>num3:
    print(f"Largest :{num1}")
elif num2>num1 and num2>num3:
    print(f"Largest :{num2}")
elif num3>num1 and num3>num2:
    print(f"Largest :{num3}")
else:
    print("Equal")
