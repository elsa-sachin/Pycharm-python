"""LINEAR SEARCH  - TIME COMPLEXITY IS VERY LARGE"""


lst=[23,5,6,7,8,23,467,75,12,88,34,13]
e=int(input("Enter the element:"))
flag=0
for i in lst:
    if i==e:
        flag=1
        break
if flag==1:
    print("Element found")
else:
    print("not found")
 # <----------------METHOD 2-------------------->
for i in lst:
    if i==e:
        print("Element found")
else:
    print("Not found")
