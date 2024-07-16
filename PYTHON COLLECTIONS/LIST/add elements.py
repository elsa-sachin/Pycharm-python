lis=[]

"""append(object) """ #add elememts to list
lis.append(4)   #cannot add multiple elements at a time
lis.append(23)
lis.append(45)
print(lis)

"""extend([object])""" #to add multiple elements at a time
lis.extend([30,45,2,1])
print(lis)

"""insert(index,object)""" # adding elements with respect to a given postion
lis.insert(4,4)


lis.insert(3,'BIG DATA')
print(lis)