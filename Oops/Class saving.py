'''
#create a class saving
class Saving:
    def __init__(self,actno,bal): #constructor
        self.actno=actno  #instant attribute
        self.bal=bal       #instant attribute
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("amount deposited successfully")
    def show_balance(self):
        return f"balance is {self.bal}"
a=int(input("enter account number"))
b=int(input("enter balance"))
s=Saving(a,b)
amt=int(input("enter amount to be deposited"))
s.deposit(amt)
print(s.show_balance())
 '''
'''
#create a class person n employee using single inheritance(attribute)
class Person:
    name="pranali"
    address="nagpur"
class Employee(Person):
    empid=123
    salary=40000

e1=Employee()
print(e1.name)
print(e1.address)
print(e1.empid)
print(e1.salary)
'''
'''
#create a class using methods inheritance
class Person:
    def getpersondata(self,name,address):
        self.name=name
        self.address=address
    def displaypersondata(self):
        print(self.name)
        print(self.address)
class Employee(Person):
    def getemployeedata(self,empid,salary):
        self.empid=empid
        self.salary=salary
    def displayemployeedata(self):
        print(self.empid)
        print(self.salary)
        
e1=Employee()
e1.getpersondata("Pranali","Nagpur")
e1.getemployeedata(123,60000)
e1.displaypersondata()
e1.displayemployeed
'''












    