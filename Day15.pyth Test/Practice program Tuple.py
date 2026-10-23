'''
# Monthly Sales Data
# A Data analyst has sales figures for 6 months stored in a tuple. Find total and average sales.
sales = (25000,32000,28000,40000,35000,45000)
total = sum(sales)
average = total/len(sales)
print("Sales: ",sales)
print("Total Sales: ",total)
print("Average Sales: ",average)
'''
'''
# Find Highest and Lowest Sales
# An analyst wants to identify the highest and lowest monthly sales.
sales = (25000,32000,28000,40000,35000,45000)
print("Highest Sales: ",max(sales))
print("Lowest Sales: ",min(sales))
'''
'''
#Sales for a Particular Month
#Sales data is stored monthwise. Display sales of the first,third,and last month
sales = (25000,32000,28000,40000,35000,45000)
print("First Month sales: ",sales[0])
print("Third Month sales: ",sales[1])
print("Last Month sales: ",sales[-1])
'''
'''
#Quarterly Sales Analysis
# A company stores monthly sales in a tuple.Calculate sales for the first qurter.
sales = (25000,30000,35000,40000,45000)
quarter1 = sales[0:3]
print("First Quarter Sales: ",quarter1)
print("First Quarter Total: ",sum(quarter1))
'''
'''
# Employee Salary Analysis
# HR provides salaries of five employees.Find the highest,lowest,and average salary.
salary = (35000,42000,28000,55000,48000)
print("Highest Salary: ",max(salary))
print("Lowest Salary: ",min(salary))
average = sum(salary)/len(salary)
print("Average Salary: ",average)
'''
'''
# Customer Age Analysis
# A data analyst has the ages of customers in a tuple. find the youngest and oldest customer.
ages = (25,32,41,28,35,52,19)
print("Youngest Customer: ",min(ages))
print("Lowest Customer: ",max(ages))
print("Total Customers: ",len(ages))
'''
'''
#Product Ratings
#A company stores customer ratings for a product.
ratings = (5,4,5,3,4,5,2,4)
print("Ratings:",ratings)
print("Highest Ratings:",max(ratings))
print("Lowest Rating:",min(ratings))
print("Average Ratings:",sum(ratings)/len(ratings))
'''
'''
#Count Customer Ratings
#An analyst wants to find how many customers gave a ratings of 5.
ratings = (5,3,4,2,5,3,5,4,5,3,5)
count = ratings.count(5)
print("Number of 5-star ratings:",count)
'''
'''
#Find Position of a Product
#Product IDs are stored in a tuple.Find the position of a particular product ID.
product_ids = (101,105,110,115,120)
product = int(input("Enter product ID:"))
if product in product_ids:
    print("Product found")
    print("Position:",product_ids.index(product))
else:
    print("Product not found")
'''
'''
#Attendance Analysis
#An analysis stores attendance percentages of employees.
attendance = (95,87,72,91,65,88,78)
print("Highest Attendance:",max(attendance))
print("Lowest Attendance:",min(attendance))
print("Average Attendance:",sum(attendance)/len(attendance))
'''
'''
#website Visitors
#A website receives the following number of visitors over seven days.
visitors=(1200,1500,1800,1300,2100,2500,2000)
print("Total Visitors:",sum(visitors))
print("Highest Visitors:",max(visitors))
print("Lowest Visitors:",min(visitors))
print("Average Visitors:",sum(visitors)/len(visitors))
'''
'''
#Check Sales Target
#A company has monthly sales in a tuple. Check whether a target value was achieved in any month.
sales = (25000,32000,28000,40000,35000,45000)
target = int(input("Enter sales target:"))
if target in sales:
    print("Target value found")
else:
    print("Target value not found")
 '''
'''
#Transaction Data
#A bank analyst has transtion amounts stored in a tuple. Calculate total transactions
#and average transaction value.
transactions = (5000,2500,10000,3500,7000)
print("Total Transaction Amount:",sum(transactions))
print("Number of Transaction:",len(transactions))
print("Average Transaction:",sum(transactions)/len(transactions))
'''
'''
#Monthly Expense Analysis
#A person's monthly expenses are stored in a tuple.
expenses=(15000,18000,12000,20000,17000,22000)
total=sum(expenses)
average=total/len(expenses)
print("Total Expense:",total)
print("Average Expense:",average)
print("Highest Expense:",max(expenses))
print("Lowest Expense:",min(expenses))
'''
'''
#Student Marks analysis
#A data analyst wants to analysis marks of a student in five subjects.
marks=(78,65,82,71,90)
total=sum(marks)
average=total/len(marks)
print("Total Marks:",total)
print("Average Marks:",average)
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))
'''
'''
#Monthly Revenue
#A company has monthly revenue:
revenue=(45000,52000,48000,60000,55000,70000)
total=sum(revenue)
average=total/len(revenue)
print("Total Revenue:",total)
print("Average Revenue:",average)
print("Highest Revenue:",max(revenue))
print("Lowest Revenue:",min(revenue))
'''
'''
#Customer Ratings
ratings=(4,5,3,5,4,2,5,3,4,5)
total=sum(ratings)
average=total/len(ratings)
count=ratings.count(5)
print("Total number of Ratings:",total)
print("Number of 5-star ratings:",count)
print("Highest ratings:",max(ratings))
print("Lowest ratings:",min(ratings))
print("Average ratings:",average)
'''
'''
#Employee Attendance
attendance=(92,85,76,95,88,67,91)
total=sum(attendance)
length=len(attendance)
average=total/len(attendance)
print("Highest attendance:",max(attendance))
print("Lowest attendance:",min(attendance))
print("Average attendance:",average)
print("Number of employees",length)
'''
'''
#Product IDs
#accept a product ID from the user and check whether it exists in the tuple.
#If it exists display its position.
products=(101,105,108,112,115,120)
pid=int(input("Enter Product ID:"))
if pid in products:
    print("Product ID exists in the tuple")
else:
    print("Product ID does not exists")
'''
'''
#Quarterly Sales
sales=(25000,30000,28000,35000,40000,38000,45000,42000,50000,48000,55000,60000)
q1 = sum(sales[0:3])
q2 = sum(sales[3:6])
q3 = sum(sales[6:9])
q4 = sum(sales[9:12])
print("1st Quarter Total=",q1)
print("2nd Quarter Total=",q2)
print("3rd Quarter Total=",q3)
print("4th Quarter Total=",q4)
'''
'''
#Customer Age Analysis
ages = (21,35,42,28,19,55,31,47)
total = len(ages)
average = sum(ages)/len(ages)
print("Youngest Customer:",min(ages))
print("Oldest Customer:",max(ages))
print("Average Age:",average)
print("Total customers:",total)
'''
'''
#sales Target
#accept a sales amount from the user and check whether that exact amount exists in the tuple.
sales=(25000,45000,38000,52000,60000)
amount=int(input("Enter sales amount:"))
if amount in sales:
    print("Sales amount exists")
else:
    print("Sales amount does not exist")
'''
'''
# Data Quality Check
#write a program to identify whether a particular age entered by the user exists in the data.
ages=(25,32,28,-5,41,150,35)
age=int(input("Enter age:"))
if age<0:
    print("Invalid age")
elif age>100:
    print("Suspicious age")
elif age in ages:
    print("Valid age and exists in the data")
else:
    print("Valid age but does not exists in the data")
'''
'''
#Transaction Analysis
transactions=(1200,5000,2500,8000,3500,10000)
total=sum(transactions)
nt=len(transactions)
average=total/nt
print("Total Transaction Amount:",total)
print("Average Transaction:",average)
print("Highest transaction:",max(transactions))
print("Lowest transaction:",min(transactions))
print("Number of transactions:",nt) 
'''
#Employee Salary Analysis
salary=(30000,45000,52000,38000,65000,42000)
total=sum(salary)
avg=total/len(salary)
print("Highest Salary:",max(salary))
print("Lowest Salary:",min(salary))
print("Average Salary:",avg)
print("Total Salary Expense:",total)









