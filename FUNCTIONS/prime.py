
def prime():
    num=int(input("Enter the number:"))
    flag=0
    for i in range(2,num):
        if(num % i==0):
            flag=1

    if flag==0:
        print("Prime")
    else:
        print(" Not Prime")





prime()