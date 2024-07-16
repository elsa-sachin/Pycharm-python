"""HINT"""


"""i=Row
j=Column
at a single row ,if u want same elements print i
whereas  if u want different elements print j"""



# for i in range(1,5):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
