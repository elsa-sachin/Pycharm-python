lst=[1,3,4,3,2,4,5,8,9,7,5,4,3,6,11,13,10,9,7,6,8,9]
#lst1=[1,4,2,9,3,13,6]
"""LOGIC:collect the elements where there is an increase or decrease in the series"""
lst1=[]
lst1.append(lst[0])
for i in range (1,len(lst)-1):
    if (lst[i-1]>lst[i]>lst[i+1]) or  (lst[i-1]<lst[i]<lst[i+1]):
        pass
    else:
        lst1.append(lst[i])

print(lst1)

