"""Write a program to accept 2 numbers and mathematical operators and perfrom operation accordingly"""
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
op=input("Enter an operator :")

if op == '+':
    print("Your Answer is: ",num1+num2)
elif op == '-':
    print("Your Answer is: ",num1 - num2)
elif op == '*':
    print("Your Answer is: ",num1 * num2)
elif op == '/':
    print("Your Answer is: ",num1 / num2)
else:
    print("Invalid operator")