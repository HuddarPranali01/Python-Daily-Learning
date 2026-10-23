#Exception handling
#Error coming when you run the program is called exception
n1=10
n2=0
result=0
try:
    result=n1/n2 #error will come if n2 is zero it will caught by except block
    print(res)
except ZeroDivisionError as e:
    print(f"error:{e}")
print(f"result:{result}")
print("Bye")