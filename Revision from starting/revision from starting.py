'''
# wap to accept a number, then print square of a number
num = int(input("Enter number "))
square = num * num
print("Square of a number = ",square)

# wap to accept 2 numbers and print addition of 2 no.
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("Addition of two numbers : ", (num1+num2))


#wap to accept length and bredth and print area of rectangle
len = int(input("Enter Length of Rectangle: "))
bread = int(input("Enter Breadth of Rectangle: "))
print("Area of Rectangle: ",(len * bread))


#wap to accept l,b,h and print volume of rectangle
len = int(input("Enter length of Rectangle: "))
bred = int(input("Enter Bredth of Rectangle: "))
height = int(input("Enter Height of Rectangle: "))
print("Volume of Rectangle: ",(len * bred * height))


#wap to accept radius, then print area of circle(pi*r*r)
radius=int(input("Enter radius"))
area=3.14 * radius * radius
print("Area of circle is :",area)
circumference = 2 * 3.14*radius
print("circumference", circumference)
'''
#----------if--elif---else------
'''
if condition:
    #code
elif condition:
    #code
else:
    #code
'''
'''
#wap to accept bill amount, calculate tax 5% if bill_amount<1000, 10% if bill_amount between 1000
# and 5000 else 15% calculate total amount(bill amount + tax)
bill_amount = float(input("Enter bill amount: "))
tax=0.0
if bill_amount < 1000 :
    tax =bill_amount *0.05
elif bill_amount >= 1000 and bill_amount <= 5000:
    tax = bill_amount *0.10
else :
    tax = bill_amount *0.15
print(f"tax amount : {tax}")
total_amount = bill_amount + tax
print(f"total_amount:{total_amount}Rs.")#jab decimal no.lena h to float lena h otherwise int lena
'''
'''
#wap to accept unit of electric meter, calculate amount depending on slack 5-units<=100,
#7-101-300, 12-greater than 300
unit = int(input("Enter unit: "))
if unit <= 100:
    amount = unit*5
elif unit <=300:
    amount = unit*7
else:
    amount = unit*12
print(f"total amount for unit : {unit} is :{amount}")
'''
'''
#wap to accept age and price calculate and print "free" if age-less than equal to 5,
#price is 150-6-65,price - 50% of price - above 65
age = int(input("Enter age of person: "))
price = 150
if age<=5:
    print("Ticket is not required")
elif age<=65:
    print(f"ticket price:{price}")
else:
    print(f"ticket price(50% consession):{price*0.5}")
'''
'''
#----------Loops-----------
#loops are used to repeatedly execute a block of code
#Types of loops: while loop and for loop
#while loop:execute a block of code untill the condition is true
syntax:
    while(condition):
        #code to be executed
        #increament or decreament
'''
'''
#program to print number from 1 to 5 using while loop
i=1
while(i<=5) :
    print(i)
    i = i+1


#print multiplication table of 9
i =1
num = int(input("Enter number")) #9
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1

#print Factorial of a number #1*2*3*4*5
i=1
fact=1
num = int(input("Enter number")) #5
while i<=5:
    fact = fact * i   # 1*1=1, 1*2=2, 2*3=6, 6*4=24,24*%=120
    i = i+1           #1+1=2, 2+1=3,3+1=4, 4+1=5, 5+1=6
print("Factorial ",fact)
'''
'''
#print sum of first 5 natural numbers using while loop
i=1
sum=0
while i<=5:
    sum = sum + i    #0+1=1,1+2=3,3+3=6,6+4=10,10+5=15
    i = i + 1        #1+1=2,2+1=3,3+1=4,4+1=5,5+1=6
print("Sum of first 5 natural numbers ",sum)

#accept 5 subject marks and print total marks using while loop
i=1
total=0
while i<=3:
    marks = float(input("Enter marks:"))  # 90 80 70
    total = total + marks                 #0+90=90,90+80=170,170+70=240
    i = i + 1  #1+1=2, 2+1=3, 3+1=4
print("Total marks",total)
'''
'''
#===========Function===========
#--------Range Function-------
#start--step--stop
#start-default 0
#step-default 1
#stop

for i in range(5):#range(0,5,1)
    print(i)

#program to print num from 5 to 1
for i in range(5,0,-1):
    print(i)

#10 to 1
for i in range(10,0,-1):
    print(i)

#program to print even no from 0 to 10
for i in range(0,11,2):
    print(i)

#odd no
for i in range(1,11,2):
    print(i)

#Print sum of first 5 natural no
sum=0
for i in range(1,6):
    sum=sum+i #1,3,6,10,15
print(sum)

#program to print sum of even no. between o and 10
sum=0
for i in range(0,11,2):
    sum=sum+i
print(sum)

#program to print sum of odd no. between 1 and 10
sum=0
for i in range(1,11,2):
    sum=sum+i
print(sum)

#program to print factorial of 5
num=5
fact=1
for i in range(1,num+1):#(1,6)
    fact=fact * i  #1*1=1,1*2=2,2*3=6,6*4=24,24*5=120
print(fact) #120

#factorial of 10
num=10
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
'''
'''
#program to accept 3 subject marks and calculate total marks using fo loop
total=0
for i in range(1,4):
    marks=int(input("Enter marks"))
    total=total+marks
print("Total marks:",total)
percentage=(total/300)*100
print("Percentage",percentage)
if percentage>=90:
    print("Grade A")
elif percentage>=75:
    print("Grade B")
elif percentage>=60:
    print("Grade C")
else:
    print("Fail")
'''
'''
#------Fuction-----
#what are different types of function argument?
#positional, keyword, default, variable length,variable keyword
#Create a function calculate having 3 arguments.
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    else:
        print("Invalid operator")
    print("Result",result)

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
operator=input("Enter +,-")
calculate(num1,num2,operator)
'''
#create a function deposit(init_amount,amount)then display the total
#create a function 

'''
#--------Keyword argument-----
#function returning a value
#function to calculate electricity bill.
def call_bill(cust_name,unit,rate):
    total=unit*rate
    prin("bill details")
    print(f'customer name :{cust_name}')
    return total
result=cal_bill(unit=250,rate=7.5,cust_name="pranali")
print(f'total amount : {result}')
'''
'''
#-------default argument-------
#function to calculate electricity bill
def cal_bill(cust_name,unit,rate=5.5):
    total=unit*rate
    print("Bill Details")
    print(f'customer name:{cust_name}')
    return total
result=cal_bill("Manish",350,8.0)
print(f'Total amount:{result}')
result=cal_bill("Ravish",350) #it will use default argument value
print(f'Total amount: {result}')
'''


'''
#-----Variable length arguments----
#If you want to send arbitary no.of arguments
def cal_sales_amount(*args):
    l=len(args)
    print(type(args))
    print("length:",l)
    total=0
    for i in range(l):
        total=total + args[i]
    print(f"total sales amount : {total}")
    
cal_sales_amount(120,500,350)
'''
'''
#function having variable length argument for fees
def cal_fees_amount(*args):
    l=len(args)
    total=0
    for i in range(l):
        total=total+args[i]
    return total
    
amount1=float(input("Enter amount 1:"))
amount2=float(input("Enter amount 2:"))
amount3=float(input("Enter amount 3:"))
ta=cal_fees_amount(amount1,amount2,amount3)
print(f"Total fees amount paid :{ta}Rs.")
'''















          