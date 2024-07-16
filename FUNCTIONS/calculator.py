
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


print("1.Additiion \n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division\n")

a=int(input("Enter the 1st number :"))
b=int(input("Enter the 2nd number :"))

ch=int(input("Enter your choice: "))

if ch==1:
    print("Addition:",add(a,b))
elif ch==2:
    print("Subtraction:",sub(a,b))
elif ch==3:
   print("Multiplication:", mul(a,b))
elif ch==4:
    print("Division :",div(a,b))
else:
    print("Inavlid choice")

