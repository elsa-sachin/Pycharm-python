f=open('sample2','r')
lis=[]

for i in f:
    lis.append(int(i.rstrip('\n')))
    #rstrip is used to remove any elements present is right side,there was \n present
    #after each element.
    """rstrip(),lstrip(),arguments are the elements to be removed"""
print(lis)
print(sum(lis))



