class Person:
    def setvalue(self,fname,lname,age,loc):
        self.fname=fname
        # we have created the variable fname as INSTANCE VARIABLE which is self.fname
        self.lname=lname
        self.age=age
        self.loc=loc
        """now we have converted all the arguments as instance variable 
        now it can be used in any methods"""

    def printvalue(self):
        print(self.fname,self.lname,self.loc,self.age)

per1=Person()
per1.setvalue('Vinay','K',22,'kochi')
per1.printvalue()


per2=Person()
per1.setvalue('Elsa','sachin',22,'Ekm')
per1.printvalue()


























