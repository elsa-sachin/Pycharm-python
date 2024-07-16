string='luminartechnolab'
vowels='aeiouAEIOU'
consonants=[]
for i in string:
    if i not in vowels:
        consonants.append(i)
print(consonants)
print(len(consonants))
