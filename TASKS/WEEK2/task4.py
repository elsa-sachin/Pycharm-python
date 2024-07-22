age=int(input("Enter your age :"))
sex=input("Enter your gender  M F : ")
days=int(input("Enter the number of days worked:"))

if 18 <= age < 30:
    if sex =='M':
        print("Wage:",days*700)
    else:
        print("Wage:",days*750)
elif 30 <= age < 40:
    if sex =='M':
        print("Wage:",days*800)
    else:
        print("Wage:",days*850)
else:
    pass

