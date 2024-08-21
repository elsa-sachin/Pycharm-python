#
# class Bank_details:
#     def set_value(self,fname,bname,accno,min_bal,bal):
#         self.fname=fname
#         self.bname=bname
#         self.accno=accno
#         self.min_bal=min_bal
#         self.bal=bal
# class deposit(Bank_details):
#     def set_value2(self,depo_amount):
#         self.depo_amount=depo_amount
#
#         print(self.fname,self.bname,self.accno,self.min_bal,self.bal+self.depo_amount)
#
# class withdraw(Bank_details):
#     def set_value3(self,wit_amount):
#         self.wit_amount=wit_amount
#
#
#         print(self.fname,self.bname,self.accno,self.min_bal,"Withdraw amount :",self.wit_amount,"Total Balance :",self.bal-self.wit_amount)
#
#
# holder1=deposit()
# holder2=withdraw()
# holder1.set_value("Elsa","Axis",1001,10,100)
# holder1.set_value2(100)
# holder2.set_value("Elsa","Axis",1001,10,100)
#
# holder2.set_value3(10)
































class Bank_details:
    min_bal=100
    def __init__(self,name,bname,acc_no,bal):
        self.name=name
        self.bname=bname
        self.acc_no=acc_no
        self.bal=bal
    def deposit(self,depo):
        self.depo=depo
        print(f"Amount deposited :{self.depo}")
        print(self.name,self.bname,self.acc_no,self.bal,Bank_details.min_bal,"New balance",self.depo+self.bal)

    def withdraw(self,draw):
        self.draw=draw
        if self.draw <= Bank_details.min_bal:
            print("The min bal is 100,cannot withdraw")
        print(f"Amount withdrew :{self.draw}")
        print(self.name, self.bname, self.acc_no, self.bal,Bank_details.min_bal,"New balance", self.bal - self.draw)


p1=Bank_details('Jco','Axis Bank',100080,100)
p1.deposit(100)
p1.withdraw(100)