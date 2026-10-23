'''
# what is Tuple?
#A tuple in python is an immutable, ordered collection of items that can store elements of different data types
#Unlike lists, tuples cannot be modified after creation, making them useful for fixed data

num=(1,2.2,"hello",True)
print(type(num))
print(num[0])
for i in num:
    print(i)
num1=(11,)
print(type(num1))

#implicit tuple
num=1,2.2,"hello" 
print(type(num))
for i in num:
    print(i)

num=1,2.2,"hello"
print(type(num))
print(num[-1])
'''
'''
#slicing tuple
num=(1,2,3,4,5)
print(num)
print(num[1:4])
print(num[:3])
print(num[3:])
print(num[::2])      #output:(1,3,5)
print(num[::-1])
'''
'''
#passing tuple to a function
def calculate(m):
    print(type(m))
    sum=0
    for i in m:
        sum +=i
    print(f"total marks ",sum)
m1=int(input("Enter marks "))
m2=int(input("Enter marks "))
m3=int(input("Enter marks "))
marks=(m1,m2,m3)
calculate(marks) #passing tuple to function
'''
#variable length argument using *args to pass arbitory no. of arguments
# def calculate(*args):
#     #print(type(args))
#     sum=0
#     for i in args:
#         sum +=i
#     print(f"total marks ",sum)
#     
# m1=int(input("Enter marks "))
# m2=int(input("Enter marks "))
# m3=int(input("Enter marks "))
# calculate(m1,m2,m3)
'''
#function returning a tuple
def calculate(r):
    area = 3.14 * r * r
    circ = 2 * 3.14 * r
    ci = (area,circ)#tuple
    return ci
radius = int(input("Enter Radius"))
result = calculate(radius)
print(f"area of circle : {result[0]}")
print(f"circumference of circle : {result[1] :.2f}")
'''
'''
#Tuple methods-> they have two built in methods
#count(x)
#index(x)
age=(18,20,18,23,24,55)
#len for length
l=len(age)
print(f"length : {l}")
num=int(input("Enter age"))
c=age.count(num)
print(f"count of age {num} in tuple : {c}")
ind=age.index(num)
print(f"index of {num} is : {ind}")
'''











