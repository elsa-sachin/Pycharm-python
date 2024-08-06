class Employee:
    company_name='Wrench'
    def setvalue(self,id,fname,lname,age,prof):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,Employee.company_name)


emp1=Employee()
emp1.setvalue(1,'Jcob','K',23,'SE')
emp1.printvalue()

emp2=Employee()
emp2.setvalue(2,'Elsa','l',23,'AI')
emp2.printvalue()