"""Python program that accepts a word from the user and reverses it."""

str=input("Enter a string:")
rev=""
n=len(str)-1
for i in range(n,-1,-1):
    rev=rev+str[i]
print(rev)