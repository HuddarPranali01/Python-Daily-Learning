#from abc import ABC abstract method
class Saving(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount+500
        print("bal with interest is",self.bal)
class Current(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("bal without interst is",self.bal)
        
s=Saving()
s.deposit(100)
c=Current()
c.deposit(200)