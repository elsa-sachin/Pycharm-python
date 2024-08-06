"""class Classname"""
"""FUNCTIONS written inside class is called METHOD"""
#self -> instance keyword ,to create a instance variable
"""instance variable can be used in any methods """
class Person:
    def reading(self):
        print("Reading a book")
    def writing(self):
        print("Write a book")

"""oBJECTS are created using Classname"""
obj1=Person()
obj1.reading()
obj1.writing()

obj2=Person()
obj2.reading()   #reference
obj2.writing()   #refernce


