# Loop is used to repeatedly execute a block of code
#Range function is used to dynamically generate sequence of numbers
'''
#using for loop print "itpreneur" 5times
for i in range(5) :
    print(f"Itpreneur : {i}")
print("bye")
'''

'''
#using for loop print numbers 1 to 5
# for i in range(1,6) :
#     print(f"i : {i}")
# print("Bye")

for i in range(51,61) :
    print(f"i : {i}")
print("Bye")
 
for i in range(20,31):
     print(f"i : {i}")
'''


# #using for loop print odd numbers between 1 to 10
# for i in range (1,11,2) :
#     print(f"i : {i}")
# print("Bye")
# 
# #Even numbers
# for i in range(50,71,2) :
#     print(f"i : {i}")
# print("Bye")

# for i in range(5,0,-1) :
#     print(f"i : {i}")
#  
# #print no from 99 to 91
# for i in range(99,90,-1) :
#     print(f"i : {i}")
    
# #19 to 1
# for i in range(19,0,-2) :
#    print(f"i : {i}")

# #10 to 0
# for i in range(10,0,-2) :
#     print(f"i : {i}")
   

'''
#accept a number and print factorial of number using for loop
num = int(input("Enter number"))
fact=1
for i in range(1,num+1) :
    fact=fact * i
print(f"factorial :",fact)
'''

'''
#wap to accept 5 subject marks using for loop and print total and percentage
total=0
for i in range(5) :
    marks=float(input(f"Enter marks for subject {i}: "))
    total = total + marks
    
percentage = (total/500)*100

print("Total marks = ",total)
print("Percentage = ",percentage,"%")
'''

'''
#wap to accept number and print table of that number using loop
num=int(input("Enter number"))

for i in range(1,11):
    
    print(num,"*",i,"=",num*i)
'''

'''
#wap to print total of first 5 natural numbers using for loop
total=0
for i in range(1,6):
    total=total+i
print(f"total of first 5 natural numbers:{total}")
'''
'''
#accept a number and print a num is prime or not
num=int(input("Enter a number")) #5
for i in range(2,num) :
    if num %i == 0:
        print("num is not prime no")
        break
#check if num is not divided by any between no.
if num == (i+1) :
    print("num is prime no")
'''

'''
#program to print prime no. between 1 to 20
for num in range(3,21) :
    for i in range(2,num) :
        if num % i == 0 :
            #print(f"{num} is not prime no")
            break
        #check if num is not divided by any between no
    if num == (i+1) :
        print(f"{num} is prime no")
'''
'''
principal=1000.0 #$1,000 starting amount
rate=0.05        #5%annual interest rate
year=4
print(f"Initial Investment : {principal}")
#Loop through each year from 1 to 4
for year in range(1,year+1):
    interest = principal * rate
    principal += interest
print(f"Year {year} : Balance=${principal:2f}")
'''     
'''
#accept password calc len, how many digits, how many special characters,if valid password
password=input("Enter Password")
d=0
s=0
l=len(password)
special="!@#$%"
print(f"length :{l}")
for p in password :
    if p.isdigit():
        d += 1
    if p in special:
        s += 1
print(f"digits : {d}")
print(f"special character : {s}")
if(l<8 or d>0) :
      if(s>0):
          print(f"password is valid")
      else :
          print("password is not valid")
else :
    print("password is not valid")
'''


#accept no. of products
noprod = int(input("Enter no. of products"))
total=0
gtotal=0
for i in range(1,noprod+1) :
    print("------------------------------")
    print(f"Enter details for product :{i}")
    #accept productname, price and quantity
    prodname=input("Enter product name")
    price=float(input("Enter product price"))
    quantity=int(input("Enter product quantity"))
    total=price*quantity
    gtotal += total
    print(f"total amount : {total}")
    print("------------------------------")
print(f"grant total amount : {gtotal}")
         










































