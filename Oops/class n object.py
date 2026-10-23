'''
#example of class attributes
class Student:
    company_name="itpnagpur"
    company_mobile=242323

s1=Student()
s2=Student()
print("s1 details")
print(s1.company_name,s1.company_mobile)
print("student details")
print(Student.company_name,Student.company_mobile)
'''
'''
class Student:
    #creating a constructor
    def__init__(self):
        print("constructor called")
s1=Student()   #it will call constructor automatically
'''

class Phone:
    #Class attribute(shared by all instances)
    device_type="Smartphone"
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("phone details")
        print(f"device type{self.device_type}")
        print(f"brand type{self.brand}")
        print(f"model{self.model}")
        print(f"price{self.price}")
    def updateprice(self,price):
        self.price=price
        print("price updated")
        self.display()
p1=Phone("mi","A12",12000)
p1.display()
p1.updateprice(15000)


