"""
          1
       1 2 1
     1 2 3 2 1
  1 2 3 4 3 2 1
"""

for i in range(1,5):
    print(" "*(4-i)*2, end=' ')
    for j in range(1,i+1):    #increasing number
        print(j,end=' ')

    for j in range(i-1,0,-1):     #decreasing numbers
        print(j,end=" ")
    print()



# for i in range(1,5):
#     for j in range(i,0,-1):
#
#     print()