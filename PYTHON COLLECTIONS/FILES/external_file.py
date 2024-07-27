"""to workout ques for any external file ,split it ie it becomes a list and them it is easy to use"""

f=open('C:\\Users\\Elsamaria Sachin\\OneDrive\\ドキュメント\\py ds\\sample4.txt','r')

for i in f:
    data=i.rstrip('\n').split(',')
    # print(data)
    age = data[3]
    loc = data[5]

    """  age above 22  ,fname,age,phono"""
    if age > '22':
        print(data[1:5])

    """  age =21 fname,age,loc """
    if age=='21':
        print(data[1::2])
    """chennai work fname.lname,age,phno"""

    if loc=='Chennai':
        print(data[1:5])

    """age above 23 and loc = chennai fname,age,loc"""
    if loc=='Chennai' and age>'23':
        print(data[1::2])




