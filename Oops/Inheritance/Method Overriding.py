#---- Simple Example of Method Overriding--- 
#child class changes the implementation of inherted method from method class
'''
class Account:
    def deposit(self):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self):
        print("deposit method of saving class")
s=Saving()
s.deposit()
'''
'''
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited, bal  is {self.bal}")
s=Saving()
s.deposit(200)
'''
'''
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited, bal  is {self.bal}")
class Current(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount
        print(f"amount deposited without interest,bal is {self.bal}")        
s=Saving()
s.deposit(200)
c=Current()
c.deposit(200)
'''
#Example of method overriding with constructor
'''
class person:
    def __init__(self,name):#constructor
        self.name=name
    def display(self):
        return f"name : {self.name}"
class student(person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"rno : {self.rno}"
s=student("Pranali",303)
print(s.display())
'''
#example of method overriding
class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name : {self.name}"
class student(person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"rno : {self.rno}"
class parttime_student(student):
    def __init__(self,name,rno,course):
        super().__init__(name,rno)
        self.course=course
    def display(self):
        print(super().display())
        return f"course : {self.course}"

#creating object
pt=parttime_student("amit",123,"python")
print(pt.display())









