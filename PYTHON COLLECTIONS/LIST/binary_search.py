""""BINARY SEARCH OVERCOME THE DISADVANTAGE OF LINEAR SEARCH"""
#lst=[9,1,6,7,3,5,10,2]
#step1: Sort the given list in asc order
#[1,2,3,5,6,7,9,10

#step2: Declare 2 variables ie low=0 and  upper=n-1
#step3:Calculate mid  lst[mid]
#3 conditions based on mid
 #1.search>lst[mid]
     #low=mid+1
  #2.search<lst[mid]
      #upper=mid-1
  #3.Search== mid
      #element found



lst=[23,56,12,78,50,21,40]
lst.sort()
print(lst)
search=int(input("Enter the element to be searched:"))
low=0
upper=len(lst)-1
flag=0
for i in range(low,upper):
        mid=(low+upper)//2
        if search >lst[mid]:
            low=mid+1
        elif search<lst[mid]:
            upper=mid-1
        elif search==lst[mid]:
            print("Element found")
            flag=1
            break
if flag==0:
    print("Not Found")




