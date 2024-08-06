"""copy the contents of sample file and write it into copy_from_sample"""

f=open("sample",'r')
f1=open("copy_from_sample",'w')
for i in f:
    f1.write(i)