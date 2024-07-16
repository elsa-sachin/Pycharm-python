"""A student will not be allowed to sit in exam if his/her attendance is less than 75%.
 Take the following input from user :No.of classes held,no.of classes attended and print the % of class attended
 ,is student allowed to sit for the exam."""


class_no=int(input("Total no.of classes held :"))
att=int(input("Enter the no. of classes attended :"))


result=(att/class_no)*100
print(result)

if(result >= 75):
    print("Allowed")
else:
    print("Not Allowed")