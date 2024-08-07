"""Functions are  used for re-usability .
The modern version of Functions are called FUNCTIONAL PROGRAMMING"""


"""4 typer of functional programming:"""

"""1.lambda :an Anoynmous(no name) func is called lamba fun"""

#variable_name=lambda arguments : operations to be done

f=lambda num1,num2:num1+num2
print(f(20,30))

a=lambda a,b,c:a*b*c
print(a(1,2,3))

sq=lambda num:num**2
print(sq(2))


"""2.map"""
#variable_name=map(function,iterable)
#variable_name=list(map(function,iterable))   if u want the o/p as list
lst=[1,2,3,4,5,6,7,8,9,10]

f=list(map(lambda num:num**2,lst))
print(f)


"""3.filter"""
#variable_name=filter(function,iterable)
#variable_name=list(filter(function,iterable))   if u want the o/p as list

even=list(filter(lambda num :num%2==0,lst))
print(even)

"""q.find odd numbers from list and find its cube;"""
odd=list(filter(lambda num :num%2!=0,lst))
print(odd)
f=list(map(lambda num:num**3,odd))
print(f)

"""4.list comprehension **"""