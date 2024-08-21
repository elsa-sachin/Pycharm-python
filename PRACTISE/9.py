"""convert string to int"""

string='5'
print(int(string))

"""convert string to list"""

string='luminar'
print(list(string))



"reversal of string"

string="hello"
s=''
for i in range(len(string)-1,-1,-1):
    s+=string[i]
print(s)

"""OR"""
string="hello"
s=''
for i in string:
    s=i+s
print(s)
