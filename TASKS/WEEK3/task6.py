"""Python program to check the validity of password input by users."""

str1=input("Enter your password :")
length=len(str1)
f=0
for i in str1:
    if (i>='0' and i<='9'):
        and 8<=length<=15  'a'<=i<='z' and 'A'<=i<='Z':
        f=1

if f==1
    print("Password is valid")
else:
    print("Password not valid")
