
class Bank_details:
    def set_value(self,fname,bname,accno,min_bal,bal):
        self.fname=fname
        self.bname=bname
        self.accno=accno
        self.min_bal=min_bal
        self.bal=bal
class deposit(Bank_details):
    def set_value2(self,depo_amount):
        self.depo_amount=depo_amount

        print(self.fname,self.bname,self.accno,self.min_bal,self.bal+self.depo_amount)

class withdraw(Bank_details):
    def set_value3(self,wit_amount):
        self.wit_amount=wit_amount


        print(self.fname,self.bname,self.accno,self.min_bal,"Withdraw amount :",self.wit_amount,"Total Balance :",self.bal-self.wit_amount)


holder1=deposit()
holder2=withdraw()
holder1.set_value("Elsa","Axis",1001,10,100)
holder1.set_value2(100)
holder2.set_value("Elsa","Axis",1001,10,100)

holder2.set_value3(10)
