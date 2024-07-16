#multiplication table of a given number

num=int(input("Enter the number:"))

i=1
while (i<=10):
    mul=i*num
    print(i,"*",num,"=",mul)
    i+=1