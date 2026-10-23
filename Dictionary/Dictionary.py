'''
#------Dictionary-----
#create a dictionary to store name, age, and city
student={"name":"lado","age":6,"city":"nagpur")
'''
'''
n= input("enter name")
a =int(input("enter age"))
c=input("enter city")
student={"name":n,"age":a,"city":c}
print(student)
 '''
'''
n= input("enter name")
a =int(input("enter age"))
c=input("enter city")
#using constructor
student=dict(name=n,age=a,city=c)
print(student)
'''
'''
#accessing from dictionary through key
#using key
n= input("enter name")
a =int(input("enter age"))
c=input("enter city")
student=dict(name=n,age=a,city=c)
print("student details")
print(f"name :{student['name']}")
print(f"age :{student['age']}")
print(f"city :{student['city']}")
'''
'''
#using get method
n= input("enter name")
a =int(input("enter age"))
c=input("enter city")
student=dict(name=n,age=a,city=c)
print("student details")
print(f"name :{student['name']}")
print(f"age :{student.get('age1')}")
print(f"city :{student['city']}")
'''
#assignment: create a dictionary named product to store product_id,product_name,
#price and stock.accept from user and store it in dictionary then display
#using[] bracket and get method
product = {}
product["product_id"] = input("Enter product id: ")
product["product_name"] = input("Enter product name: ")
product["price"] = float(input("Enter price: "))
product["stock"] = int(input("Enter stock: "))










