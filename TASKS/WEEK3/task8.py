"""a, b, c = 0, 0, 0 . Write a python program to print all permutations using those three variables

"""
import itertools
from itertools import permutations

a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))

print(permutations(a,b,c))