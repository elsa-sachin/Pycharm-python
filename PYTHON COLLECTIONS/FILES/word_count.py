dic={}
st=''
f=open('para','r')
for i in f:
    st+=i
for j in st.split():
    if j not in dic:
        dic[j]=1
    else:
        dic[j]+=1
print(dic)
for k,v in dic.items():    #to get the key value pair seperately
    print(k,':',v)
"""<------------------------------------------------------------METHOD2----------------------->"""
# dic = {}
# f = open('para', 'r')
# for i in f:
#     data=i.rstrip('\n').split()
#     for j in data:
#         if j not in dic:
#             dic[j] = 1
#         else:
#             dic[j] += 1
# print(dic)
