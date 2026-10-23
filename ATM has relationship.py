'''
#------ATM OPERATION-----
class Customer:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
    def add_account(self,account):
        self.accounts.append(account)
#creating a class account
class Account:
    def __init__ (self,account_no,balance=0):
        self.account_no = account_no
        self.balance = balance
#execution of program start here
c=Customer(123,'kashish')#it will call customer class constructor
a=Account(1,1000)#it will call account class constructor
c.add_account(a)
print("customer details")
print(f"customer id : {c.customer_id}")
print(f"customer name: {c.name}")

#Display account details through customer object
print(f"Account no : {c.accounts[0].account_no}")
print(f"Balance : {c.accounts[0].balance}")
'''
class Student:
    def __init__ (self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.addresses = []
    def add_address(self,address):
        self.addresses.append(address)
class Address:
    def __init__(self,locality,city,state):
        self.locality = locality
        self.city = city
        self.state = state
s = Student(123,'Pranali')
a = Address("Kamptee","Nagpur","Maharashtra")
s.add_address(a)
print("Student details")
print(f"roll_no : {s.roll_no}")
print(f"student name: {s.name}")

#Display account details through customer object
print(f"locality : {s.addresses[0].locality}")
print(f"city : {s.addresses[0].city}")
print(f"state : {s.addresses[0].state}")


