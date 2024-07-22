"""Write a python program to check if a string is a valid identifier or not.An identifier is valid if it
starts with a letter(a-z,A-Z) or an underscore followed by zero or more letters,underscores or digits(0-9)
"""

str=input("Enter a string:")

count=0
for i in str:
    flag=0
    if count==0:
        if (i >= '0' and i<='9'):
            flag=1
            break
    if ('a'<=i<='z') or ('A'<=i<='Z') or  (i >='0 'and i<='9') or (i=='_'):
        pass
    else:
        flag = 1
        break
    count+=1

if(flag==0):
    print("Valid identifier")
else:
    print("Not valid")