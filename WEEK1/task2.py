"""Write a python program to find all valid identifiers in a given string.
Assume that identifiers are seprated by spaces."""

str=input("Enter a string :")

for i in str:
    flag=0
    if (i >= '0' and i<='9'):

        continue

    if ('a'<=i<='z') or ('A'<=i<='Z') or (i==0) or (i >='0 'and i<='9') or (i=='_'):
        if (i == " "):
            print()
            print(i,end=" ")
        else:
            print(i,end="")
