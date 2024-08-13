lower=int(input("Enter the lower limit:"))
upper=int(input("Enter the upper limit:"))

# for i in range(lower,upper+1):
#     flag = 0
#     for j in range(2,i):
#         if i % j == 0:
#             flag = 1
#             break
#
#     if flag==0:
#         print(i)



i=2
while(lower<=upper):
    flag=0
    while(i<lower):
        if(lower%i==0):
            flag=1
            break

        i+=1
    lower+=1

    if flag==0:
        print(i)

