lst=[34,34,56,11,12,78,99,34,56,78,2,4,5,6,90]

"""deleting  an  element from a list -remove()-- passing element (main diff btw pop())"""


lst.remove(99)
print(lst)
lst.remove(90)
print(lst)
lst.remove(34)
print(lst)

"""deletes an element from an index-pop()--passing index (main diff btw remove())"""

lst.pop()   # deletes the last element
lst.pop(0)
print(lst)

