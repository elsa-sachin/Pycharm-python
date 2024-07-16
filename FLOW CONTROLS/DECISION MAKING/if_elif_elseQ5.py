""" Calculate electricity bill"""

units=int(input("Enter the no.of units:"))

if(units <= 100):
    rs=0
elif(101 <= units <= 200 ):
    rs= (units-100) *5
elif(units >200):
    rs=(units-200)*10+500
print("Bill",rs)
