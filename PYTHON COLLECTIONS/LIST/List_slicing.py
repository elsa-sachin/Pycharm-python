
"""LIST SLICING :  to get elements from a particular range"""


lst=[10,11,5,4,16,20,25,7,1,2,3,12,50]

"""SYNTAX
lst[start:stop-1]"""

print(lst[1:4])
print(lst[8:13])
print(lst[4: ])    # index=4 to end of the list
print(lst[ :7])    #index=0 to index=6
print(lst[:])       # complete list

"""[start:stop-1:step/incremeenr/decreemnet]"""
print(lst[2:8:2])
print(lst[1:9:3])

print(lst[1::3])
print(lst[:8:2])
print(lst[::4])

"""POSITIVE INDEXING : LEFT - RIGHT  : 0 TO N-1"""
"""NEGATIVE INDEXING : RIGHT - LEFT   :-1 TO -N"""

print(lst[-1])
print(lst[-6])