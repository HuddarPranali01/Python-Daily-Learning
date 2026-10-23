'''
# Q1. Class and Object (4 marks)
#Create a class Student with attributes name and marks. Add a method display() that prints both.
#Create two objects and call display() on each.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
s1=Student("Pranali",80)
s2=Student("Nidhi",85)
s1.display()
s2.display()

# Q2. Methods with Calculation (5 marks)
# Create a class Rectangle with attributes length and width. Add methods area() and perimeter().
# Create an object with length 8 and width 5, and print both results.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Area:",self.length * self.width)
    def perimeter(self):
        print("Perimeter:", 2* (self.length + self.width))

r = Rectangle(2,5)
r.area()
r.perimeter()

# Q4. Inheritance (6 marks)
# Create a parent class Person with attributes name and age and a method display().
# Create a child class Student that inherits from Person, adds a roll_no attribute, and uses
# super() in its constructor. Override display() in Student so it prints all three details.
# Create a Student object and call display().
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Person):
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def display(self):
        print("Name: ", self.name)
        print("Age: ",self.age)
        print("Roll No: ",self.roll_no)

s1=Student("Laranya",6,9)
s1.display()

# Q3. Constructor with Default Value (4 marks)
# Create a class Counter whose constructor sets count = 0. Add methods increment(), decrement()
# and show(). Call increment() three times, decrement() once, then show the final count.
class Counter:
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def decrement(self):
        self.count -= 1
        
    def show(self):
        print("Final count:",self.count)
c1 = Counter()

c1.increment()
c1.increment()
c1.increment()
c1.decrement()

c1.show()
'''
Q5. Encapsulation (6 marks)
Create a class BankAccount with a private attribute __balance starting at 0. Add these methods:
•	deposit(amount): adds to the balance
•	withdraw(amount): subtracts only if the balance is sufficient, otherwise prints “Insufficient balance”
•	get_balance(): returns the balance
Deposit 1000, withdraw 400, try to withdraw 800, and print the final balance






