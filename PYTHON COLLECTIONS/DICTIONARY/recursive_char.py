pattern='ABCDFBCFGHJABCD'
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(f"{i} first recursive character")
        break

