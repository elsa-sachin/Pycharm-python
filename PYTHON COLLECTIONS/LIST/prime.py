lst=[10,2,5,15,11,7,20,30,23,61,75]
prime=[]

for i in lst:
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        prime.append(i)

print(prime)