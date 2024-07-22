"""Acccept 3 sides of triangle and check whether it is equilateral,iscoclese or scalene """

side1=int(input("Enter the first side:"))
side2=int(input("Enter the second side:"))
side3=int(input("Enter the third side:"))

if side1==side2 and side1==side3 and side2==side3:
    print("Equilateral triangle")
elif side1==side2 or side1==side3 or side2==side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")