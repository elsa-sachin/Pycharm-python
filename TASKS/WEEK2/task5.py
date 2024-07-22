"""A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
"""

quant=int(input("Enter the amount of quantity purchased: "))
cost=quant*100
if cost >1000:
    tot_cost=cost*0.1
    print(f" Total cost after discount {tot_cost}")
else:
    print(f"Total cost without discount {cost}")