"""Python program to check the validity of password input by users."""

str1=input("Enter your password :")
length=len(str1)
l=u=d=p=0
if (length >= 8):
    for i in str1:

        if (i.islower()):
            l += 1
        if (i.isupper()):
            u += 1
        if (i.isdigit()):
            d += 1

        # counting the mentioned special characters
        if not i.isalnum():
                p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(str1)):
    print("Valid Password")
else:
    print("Invalid Password")