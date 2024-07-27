"""find max temp of each district"""
dic={}
f=open("C:\\Users\\Elsamaria Sachin\\OneDrive\\ドキュメント\\py ds\\temper.txt",'r')
for i in f:
    data=i.rstrip('\n').split(',')
    district=data[0]
    temp=data[1]

    if district not in dic:
        dic[district]=temp
    else:
        if temp>dic[district]:  #if the  new temp>old temp
            dic[district]=temp

print(dic)
