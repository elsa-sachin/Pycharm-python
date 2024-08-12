"""all problems done using list can be done in one line using
list comprehension ,optimization"""

"""METHOD 1"""
#adding a range of elements into a list with no condition

#variablename=[print range]

# lst=[i for i in range(1,51)]
# print(lst)
# lst1=[i for i in range(1,21)]
# print(lst1)
# lst=[i**2 for i in range(1,26)]
# print(lst)
"""<------------------------------------------------------------------------------------------->"""
"""METHOD 2"""
#adding a range of elements into a list based on a condition

#[print range if condition]
lst=[i for i in range(1,51) if i%2==0]
print(lst)

"""<------------------------------------------------------------------------------------------->"""
"""METHOD 3"""
#adding a range of elements based on more than one condition



lst=["small" if i <=15  if 16<=i<=35 (i,'med') else (i,"large") for i in range(1,51)]
"""<------------------------------------------------------------------------------------------->"""