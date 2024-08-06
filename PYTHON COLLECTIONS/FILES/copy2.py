f=open('fruits','r')
f1=open('fruits_apple','w')
for i in f:
    if i.rstrip('\n') != 'apple':
        f1.write(i)
    else:
        pass