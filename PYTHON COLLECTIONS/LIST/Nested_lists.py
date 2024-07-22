"""muliptle lists within a list"""


lst=[[101,'Leah','P',25,'Developer',1000],
     [102,'Rose','K',23,'Python',1200],
     [103,'Kevin','L',22,'C++',1230],
     [104,'Harry','M',28,'C',2000],
     [105,'Ismail','N',29,'Python',1200],
     [106,'Yakub','J',21,'Bigdata',2300],
     [107,'Ezra','E',26,'Analytics',2900]]

# for value in lst:
#     print(value) # prints the nested lists ,seprately
#
# for value in lst:
#     print(value[1:5])  #f_name.last_name,age_prof
#
# for value in lst:
#     print(value[1::2])  #fname,age,sal
"""<----------------------------------------------------------------------------->"""
# for value in lst:
#     if value[3]>27:
#         print(value[1:5])
#
"""<----------------------------------------------------------------------------->"""
# for value in lst:
#     if value[3]==25:
#         print(value[1::2])
"""<----------------------------------------------------------------------------->"""

# for value in lst:
#     if value[4]=='Bigdata':
#         print(value[1:])
"""<----------------------------------------------------------------------------->"""

# for value in lst:
#     if value[5]>1500:   value[-1]
#         print(value[1:5])

"""<----------------------------------------------------------------------------->"""
# for value in lst:
#     if value[3]>=27 and value[4]=='Bigdata':
#         print(value[1:4])
"""<----------------------------------------------------------------------------->"""
s=0
for value in lst:
    s+=value[5]
print(s)




