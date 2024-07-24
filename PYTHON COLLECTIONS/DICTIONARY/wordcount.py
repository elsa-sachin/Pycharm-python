"""INTERVIEW QUES- to find the frequency of a word"""

line='cat bat rat mango cat rat bat mango mango rat bat'
# cat,3
# bat,3
# mango,3
dic={}
for i in line.split():
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


