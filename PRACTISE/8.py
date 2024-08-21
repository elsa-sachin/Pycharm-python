# item=int(input("Enter the element to be searched: "))
#
# lst=[12,90,67,89,23,5,12,34,90,12]
#
# for i in lst:
#     f=0
#     if i==item:
#         f=1
#         break
# if f>0:
#     print("Element found ")
# else:
#     print("Not found")





item=int(input("Enter the element to be searched:"))
lst=[12,91,67,89,23,5,32,34,90,21]
lst.sort()
print(lst)
low=0
upper=len(lst)-1
f=0
while(low<=upper):
    mid=low+upper//2
    if item < lst[mid]:
        upper=mid-1
    elif item > lst[mid]:
        low=mid+1
    elif item==lst[mid]:
        f=1
        break

if f>0:
    print("Element found")
else:
    print("Not found")