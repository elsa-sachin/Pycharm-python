lst=['apple','mango','grape','kpl','mnp','ipl','isl']
vowels='aeiouAEIOU'
vow=[]
for word in lst:
    for char in word:
        if char in vowels:
            vow.append(word)
            break
        else:
            pass
print(vow)

