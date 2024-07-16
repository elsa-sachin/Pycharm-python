sub1=int(input("Enter the marks for subject1 :"))
sub2=int(input("Enter the marks for subject2 :"))
sub3=int(input("Enter the marks for subject3 :"))
sub4=int(input("Enter the marks for subject4 :"))

total=sub1+sub2+sub3+sub4
print("Total Marks :",total)

if(total >= 180 ):
    print("A+")
elif(total>= 160 and total <= 179 ):
    print("A")
elif(total>=140 and total<=159 ):
    print("B+")
elif(total>=120 and total <=139 ):
    print("B")
elif(total>= 100 and total <=119):
    print("C+")
else:
    print("Fail")
