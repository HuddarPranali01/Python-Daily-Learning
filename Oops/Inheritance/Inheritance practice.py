'''
#-----Single Inheritance----
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
    
class Employee(Person):
        def __init__(self,name,age,salary):
            super().__init__(name,age)
            self.salary = salary
            
        def display(self):
            super().display()
            print(f"Salary:{self.salary}")
            
e1 =Employee("Pranali",33,40000)
e1.display()
'''
'''
class Vehicle:
    def fuel_type(self):
        print("Uses petrol/diesel")
        
class Car(Vehicle):
    def num_wheels(self):
        print("4 wheels")
c1 = Car()
c1.fuel_type()
c1.num_wheels()
'''
#Hierarchical Inheritance
class Shape:
    def info(self):
        print("This is a shape")
class Circle(Shape):
    def area(self):
        radius = float(input("Enter radius:"))
        















