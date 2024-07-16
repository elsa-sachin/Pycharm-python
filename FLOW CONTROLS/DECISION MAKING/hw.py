#current yr
#current date
# current month


# birth_yr
# birth month
# birth date




#print age



c_yr=int(input("Enter the current year :"))
c_date=int(input("Enter the current date"))
c_month=int(input("Enter the current month :"))


b_yr=int(input("Enter the birth year :"))
b_date=int(input("Enter the birth date"))
b_month=int(input("Enter the birth month :"))



years=c_yr-b_yr

if( c_month<b_month):
    years-=1
else:
    if(c_month==b_month):
        if(c_date<b_date):
            years-=1
print(years)