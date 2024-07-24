
"""SET OPERATIONS   - UNION,INTERSECTION,DIFFERENCE"""

set1={1,2,3,4,5,6,7,8,9,10}
set2={5,6,7,8,9,10,11,12,13,14}


"""<--------------------UNION(combining 2 sets,no duplicate values cuz set does not support duplicate values)------------------------------------------->"""
set3=set1.union(set2)
print(set3)
"""<--------------------INTERSECTION(common elements in 2 sets)------------------------------------------->"""
set4=set1.intersection(set2)
print(set4)
"""<--------------------DIFFERENCE(set1-set2,element present in set1 and not present set2)------------------------------------------->"""
set5=set1.difference(set2)
set6=set2.difference(set1)
print(set5)
print(set6)
