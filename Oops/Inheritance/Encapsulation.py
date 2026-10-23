'''
#Encapsulation:
#Example of private attribute 
class Account:
    def __init__(self,actno,balance):
        self.actno=actno #public attribute
        self.__balance=balance #private attribute
        
a=Account(111,1000)
print(a.actno)
#print(a.balance)
print(a._Account__balance) #accessing private attribute using name mangling
#example:
class Student:
    def __init__(self,name,rno):
        self.name=name
        self.__rno=rno
s=Student("Ovi",4)
print(s.name)
print(s._Student__rno)
'''
'''
#Encapsulation: private attribute n private method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno #public attribute
        self.__balance=balance #private attribute
    #private method
    def __showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(111,1000)
print(a.actno)
#print(a.balance) error
print(a._Account__balance) #accessing private attribute using name mangling
a._Account__showbalance()
'''
'''
#Encapsulation: private attribute n public method 
class Account:
    def __init__(self,actno,balance):
        self.actno=actno #public attribute
        self.__balance=balance #private attribute
    #public method 
    def showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(765,1000)
print(a.actno)
a.showbalance()
'''
'''
#Encapsulation: protected attribute n public method 
class Account:
    def __init__(self,actno,balance):
        self.actno=actno #public attribute
        self._balance=balance #protected attribute
class Saving(Account):        
    def showbalance(self):
        print(f"balance is, {self._balance}")
        
a=Saving(111,1000)
print(a.actno)
a.showbalance()
'''
