"""Method is replaced by a Constructor,values can be passed within object"""

class Student:
    def __init__(self,id,fname,lname,age):  #__init__ is the constructor
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age

    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age)


stu1=Student(101,'Vinay','K',20)
stu1.printvalue()