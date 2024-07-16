"""INTERVIEW"""


string='luminartechnolab'
vowels='aeiouAEIOU'

vow=[]

for i in string:
        if i in vowels:
            vow.append(i)

print(vow)
print(len(vow))
