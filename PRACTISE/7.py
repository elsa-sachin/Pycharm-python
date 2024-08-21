string=input("Enter a string :")
small=upper=num=f=0

if len(string)>=8:
    for i in string:
        if 'a'<=i<='z':
            small+=1
        if 'A'<=i<='Z':
            upper+=1
        if '0'<=i<='9':
            num+=1
        if not i.isalnum():
            f+=1
else:
    len=0

if small >=1 and upper >=1 and num>=1 and f>=1:
        print("Valid")

elif small==0:
    print("Include lowercase letters ",small)
elif upper==0:
    print("Include uppercase letters")
elif num==0:
    print("Include numbers")
elif f==0:
    print("Inculde special characters")
else:
    print("Not valid")

