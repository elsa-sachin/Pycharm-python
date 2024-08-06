class Student:
    collname='RSET'  #static variable
    def setvalue(self,id,fname,lname,age,course):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course


    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.course,Student.collname)
        """for prinitng static var use classname.varname"""


 st1=Student()
st1.setvalue(1,'Jacob','Eldhose',23,'AI')
st1.printvalue()

st2=Student()
st2.setvalue(2,'Yacob','E',23,'AI')
st2.printvalue()

st3=Student()
st3.setvalue(3,'Elsa','c',23,'Python')
st3.printvalue()

st4=Student()
st4.setvalue(4,'Jake','B',23,'AI')
st4.printvalue()

st5=Student()
st5.setvalue(5,'Zera','A',23,'AI')
st5.printvalue()

"""instance variable is also called dynamic variable i.e keeps changing for every object"""
"""constant values are called static variables in this case collname is static """