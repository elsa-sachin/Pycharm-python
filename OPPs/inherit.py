class Personal_data:
    def data(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age

class Professional_data(Personal_data):
    def data1(self,prof,dept,salary,loc):
        self.prof=prof
        self.dept=dept
        self.salary=salary
        self.loc=loc
        print(self.id,self.fname,self.lname,self.age,self.prof,self.dept,self.salary,self.loc)

obj1=Professional_data()
obj1.data(1,"Elsa","K",23)
obj1.data1("AI engineer","AI",2000,"kakkanad")