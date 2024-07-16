""" A company decided to give a bonus of 5% to employee if his?her year of service is more than
5 year.Ask the user for their salary and year of service and print the net bonus amount"""


sal=int(input("Enter your salary :"))
exp=int(input("Enter the years of service :"))

if (exp >=5):
    bonus=sal*0.05
    print("Net Bonus Amount :",bonus)
else:
    print("No Bonus ")