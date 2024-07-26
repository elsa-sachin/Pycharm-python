"""to read the file from the same package(directory)"""

# f=open('sample','r')
# for i in f:
#     print(i,end="")

"""to read the file from different package,take its absolute path"""
f=open('/home/elsamaria/PycharmProjects/Data_science_june/PYTHON COLLECTIONS/DICTIONARY/words','r')
for i in f:
    print(i,end="")
