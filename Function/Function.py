#-----Function----
'''
#create a fuction display to print("hello from Itp")
def display():
    print("Hello from Itp")
    print("Your current batch is DADS")
print("calling the function display")
display()
print("again calling the function display")
'''
'''
#function square with one parameter to square the number
def square(num):
    sq=num*num
    return sq
num=int(input("Enter number"))
result = square(num)
print(f"square of a number is :{result}")
'''
'''
#function to print factorial  of a number
def factorial(num):
    fact=1
    while(num>0):
        fact = fact * num
        num -=1
    return fact
n=int(input("enter number"))
result=factorial(n)
print(f"factorial : {result}")
'''
'''
#create a function calculate with 3parameter to accept 2no and 1 operator
def calculate(n1,n2,op):
    result=0
    if op == '+' :
        result = n1+n2
    elif op == '-' :
        result = n1-n2
    elif op == '*' :
        result = n1*n2
    else :
        print("Invalidc operator")
    print(f"result is - {result}")
num1=int(input("Enter number1"))
num2=int(input("Enter number2"))
operator=input("Enter operator(+,-*)")
calculate(num1,num2,operator)
'''
'''
#functio  to check username and password
def check(username,password) :
    if username=="admin" and password=="admin123" :
        print("Login Successfull")
    else:
        print("Invalid username or password")
u=input("Enter username")
p=input("Enter password")
check(u,p)
'''

'''
#function calculate with 3argument to accept 3subject marks and print total and percentage and grade
def calculate(m1,m2,m3) :
    total = m1+m2+m3
    percentage = total/3
    if percentage >= 90 :
        grade = "A"
    elif percentage >=75 :
        grade = "B"
    elif percentage >=60 :
        grade = "C"
    elif percentage >=40 :
        grade = "D"
    else :
        grade = "F"
    print("Total = ",total)
    print("Percentage = ",percentage)
    print("Grade = ",grade)
calculate(80,70,75)
'''
#function calculate with one argument to accept unit and calculate bill_amount
#0-100 ->8rs
#101-300 ->12rs
#>300 ->15rs
def calculate(unit):
    if unit <= 100 :
        bill = unit*8
    elif unit <= 300 :
        bill = unit*12
    else :
        bill = unit*15
    print("Bill Amount = ",bill)
unit = int(input("Enter units:"))
calculate(unit)













