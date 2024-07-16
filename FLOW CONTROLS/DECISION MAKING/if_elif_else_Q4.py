price=int(input("Enter the amount :"))

if(price > 100000):
    tax=price * 0.15
elif(price >= 50000 and price <= 100000):   #50000 <= price <=100000
    tax=price* 0.10
else:
    tax=price*0.05
print("Tax Amount :",tax)

