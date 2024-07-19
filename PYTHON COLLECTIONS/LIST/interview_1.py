lst=[6,10,8,12,20,4,15,4,1]
lst1=[]

for i in lst:
    lst1.append(sum(lst)-i)

print(lst1)