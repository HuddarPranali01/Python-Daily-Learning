
#-----inheritance----
#Hiererchical inheritance ->1 parent class and 2child class is hiererchical inheritance
class Account: #parent class
    def __init__(self,act_no,bal):
        self.act_no = act_no
        self.bal = bal
    def show_balance(self):
        return f"balance is {self.bal}"
class Saving(Account): #child class
    interest = 500
    def deposit(self,amount):
        self.bal = self.bal + amount + self.interest
        return f"amount deposited with interest, bal is {self.bal}"
class Current(Account): #child class
    def deposit(self,amount):
        self.bal = self.bal + amount
        return f"amount deposited without interest, bal is {self.bal}"
s = Saving(123,1000)
print(s.deposit(100))
print(s.show_balance())

c = Current(124,1000)
print(c.deposit(500))
print(c.show_balance())

'''
#-----Multi level inheritance with attribute---- 
class Person:
    name = "Namita"
class Employee(Person):
    salary = 50000
class Parttime_Employee(Employee):
    no_hours = 6
    
p = Parttime_Employee()
print(f"name {p.name}")
print(f"salary {p.salary}")
print(f"no of hours {p.no_hours}")
'''
'''
#-----Multi level inheritance with method-----
class Person:
    def get_name(self,name):
        self.name = name
        return self.name
    class Employee(Person):
        def get_salary(self,salary):
            self.salary = salary
            return self.salary
class Parttime_Employee(Employee):
    def get_hours(self,hours):
        self.no_hours = hours
        return self.no_hours
p = Parttime_Employee()
print(f"name{p.get_name('Pranali')}")
print(f"salary{p.get_salary(20000)}")
print(f"no of hours{p.get_hours(5)}")
 '''           















    
