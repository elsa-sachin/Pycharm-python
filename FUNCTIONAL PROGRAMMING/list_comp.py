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

# lst=[i for i in range(1,51) if i%2==0]
# print(lst)

# lst=[i**3 for i in range(1,31) if i%2!=0]
# print(lst)

# lst=[i for i in range(1,101) if i%3==0 and i%5==0]
# print(lst)

"""<------------------------------------------------------------------------------------------->"""
"""METHOD 3"""
#adding a range of elements based on more than one condition   NO ELIF

# [print1 if condtion 1 else print2 range]   print1 excutes when condition1 is satisfied else print 2 is executre
# [print1 if condtion 1 else print2 if condition 2  else print 3 range] same as above but print2 executes when conditiion 2 is satisfied


# lst=[i**2 if i%2==0 else i**3 for i in range(1,51) ]
# print(lst)

# lst=[(i,"even") if i%2==0 else (i,"odd") for i in  range(1,41)]
# print(lst)


# lst=[(i,"small") if 1<=i<=15 else (i,"medium") if 16<=i<=35 else (i,"large") for i in range(1,51)]
# print(lst)


# string='luminartechnolab'
# vowels='AEIOUaeiou'
# lst=[i for i in string if i in vowels]
# print(len(lst))


# string='luminartechnolab'
# vowels='AEIOUaeiou'
# lst=[i for i in string if i not in vowels]
# print(len(lst))

# lst=[i for i in range(1,1001) if i%8==0]
# print(lst)

lst=[i for i in range(1,1001) if "6" in str(i)]
print(lst)

# string='luminar te ch nolab'
# lst=[i for i in string if i ==' ']
# print(len(lst))

# string='Practice list comprehension problem to drill your head'
#
# lst=[i for i in string.split()  if len(i) <=5 ]
# print(lst)








"""<------------------------------------------------------------------------------------------->"""