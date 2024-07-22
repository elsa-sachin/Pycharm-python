"""Write a python program to find all valid identifiers in a given string.
Assume that identifiers are seprated by spaces."""

string = input("Enter the sentence :")
string+=' '
identifier = ''
for i in string:
    if i != ' ':
        identifier += i
    else:
        count=0
        for j in identifier:
            flag = 0
            if count==0:
                if ('0' <= j <= '9'):
                    flag=1
                    break
            if ('a' <= j <= 'z') | ('A' <= j <= 'Z') | ('0' <= j <= '9') | (j == '_'):
                pass
            else:
                flag=1
                break

        if (flag == 0):
            print(f"{identifier} is Valid")
        else:
            print(f"{identifier} is invalid")
        identifier = ''

