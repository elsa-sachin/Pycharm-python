lst=[1,1,3,3,4,5,6,10,10,30,2,3,4,50]
lst1=[]

for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)