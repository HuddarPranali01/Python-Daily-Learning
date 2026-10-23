'''
#---------Keyword Argument------------
def calculate(n1,n2,op):
    result=0
    if op == '+' :
        result = n1 + n2
    elif op == '-' :
        result = n1 - n2
    elif op == '*' :
        result = n1 * n2
    elif op == '/' :
        result = n1 / n2
    return result
num1 = int(input("Enter number1"))
num2 = int(input("Enter number2"))
operator = input("Enter operator( +,-,*,/)")
r= calculate(n1=num1,op=operator,n2=num2) #keyword arguments
print(r)
'''


#-----Default Argument------
#These are parameters with default values, used if no argument is provided for them.

'''
def contact(fullname,phonenumber,city="nagpur"):
    print("--------contact details---------")
    print(f"full name : {fullname}")
    print(f"phone number : {phonenumber}")
    print(f"city : {city}")

#ACCEPT DETAILS
fn=input("Enter full name")
ph=input("Enter phone number")
ch=input("Do you want to enter city press or no")
if ch=="yes" :
    city=input("Enter city")
    contact(fn,ph,city)
else :
    contact(fn,ph)
'''

#-----Variable-Length Arguments------
#These allow a function to accept an arbitar number of arguments. there are two types:
#*arg:collects extra positional arguments into a tuple.
#kwargs: collects extra keyword arguments into a dictionary.














