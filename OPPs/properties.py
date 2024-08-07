


"""1.INHERITANCE"""
#inhereting the properties of class ie.parent class
#inherited by the child class
#the classes inherit instance variables ,methods
class A:  #PARENT CLASS
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)
class B(A):  #CHILD CLASS  #B inherited A's feature such as method
    def printb(self,num2):
        self.num2=num2
        print("inside class B",self.num2)

obj1=B()
obj1.printa(20)



"""2.POLYMORPHISM"""


"""3.ENCAPSULATION"""

"""4.DATA BINDING"""