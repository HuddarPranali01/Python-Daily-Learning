#print("------practice program function--------")
'''
# Calculate Total Sales
# A company has sales from three different days. Create a function to calculate total sales.
def total_sales(s1,s2,s3):
    total = s1 + s2 + s3
    print("Total Sales :",total)
s1 = float(input("Enter Monday Sales:"))
s2 = float(input("Enter Tuesday Sales:"))
s3 = float(input("Enter wednesday Sales:"))
total_sales(s1,s2,s3)
'''
'''
#Calculate Average Sales
#An analyst wants to find the average sales fo rthree days.
def average_sales(s1,s2,s3):
    avg=(s1+s2+s3)/3
    print("Average Sales:",avg)
s1 = float(input("Enter sales1 : "))
s2 = float(input("Enter Sales2 : "))
s3 = float(input("Enter Sales3 : "))
average_sales(s1,s2,s3)
'''
'''
#Find Highest Sales
#A sales  analyst wants to identify the highest sales among three days.
def highest_sales(s1,s2,s3):
    if s1>s2 and s1>s3 :
        print("Highest sales : ",s1)
    elif s2>s1 and s2>s3 :
        print("Highest Sales: ",s2)
    else :
        print("Highest sales : ",s3)
s1 = float(input("Enter sales1: "))
s2 = float(input("Enter sales2: "))
s3 = float(input("Enter sales3: "))
highest_sales(s1,s2,s3)
'''
'''
#Sales performance
# A company wants to classify an employee's sales performance.
def sales_performance(sales):
    if sales >=100000:
        print("Excellent performance")
    elif sales >= 50000:
        print("Good performance")
    elif sales >= 25000:
        print("Average performance")
    else :
        print("Poor performance")
sales = float(input("Enter total sales: "))
sales_performance(sales)
'''
'''
# Calculate Profit or Loss
# A data analyst needs to determine whether a bussiness trasaction resulted in profit or loss.
def profit_loss(cost_price,selling_price):
    if selling_price>cost_price :
        profit = selling_price - cost_price
        print("Profit: ",profit)
    elif cost_price>selling_price :
        loss = cost_price - selling_price
    else :
        print("No profit, No loss")
cost = float(input("Enter cost price: "))
selling = float(input("Enter selling price: "))
profit_loss(cost,selling)
'''
'''
#Employee Salary Analysis
# HR wants to categorize employees based on their salary.
def salary_category(salary):
    if salary >= 80000:
        print("High Salary")
    elif salary >= 40000:
        print("Medium Salary")
    else :
        print("Low Salary")
salary = float(input("Enter employee salary: "))
salary_category(salary)
'''
'''
# Student Performance Analysis
# An analyst wants to categorize students based on their average marks.
def student_performance(avg) :
    if avg >=75 :
        print("Excellent")
    elif avg >=60 :
        print("Good")
    elif avg>=40 :
        print("Average")
    else :
        print("Poor")
avg = float(input("Enter average marks: "))
student_performance(avg)
'''
'''
#Customer Spending Category
#A company wants to classify customers based on their total spending.
def customer_category(amount):
    if amount >=100000:
        print("Premium Customer")
    elif amount >= 50000:
        print("Gold Customer")
    elif amount >= 10000:
        print("Silver Customer")
    else :
        print("Regular Customer")
amount = float(input("Enter customer spending : "))
customer_category(amount)
'''
'''
#Calculate Monthly Expense
#A data analyst wants to calculate the total monthly expenses of a person.
def total_expense(rent,food,travel,shopping):
    total=rent+food+travel+shopping
    print("Total Monthly Expense : ",total)
rent=float(input("Enter rent: "))
food=float(input("Enter food expense: "))
travel=float(input("Enter travel expense: "))
shopping=float(input("enter shopping expense: "))
total_expense(rent,food, travel,shopping )
'''
'''
#Expense Category
#A financial analyst wants to categorize a person's monthly expense.
def expense_category(expense):
    if expense >= 50000:
        print("Very High Expense")
    elif expense >= 30000:
        print("High Expense")
    elif expense >=15000:
        print("Medium Expense")
    else:
        print("Low Expense")
expense = float(input("Enter Monthly Espense:"))
expense_category(expense)
'''
'''
#Attendence Analysis
# An HR analyst wants to classify an employee based on attendnce percentage. 
def attendence_status(attendence):
    if attendence >= 90:
        print("Excellent Attendence")
    elif attendence >= 75:
        print("Good Attendence")
    elif attendence >=60:
        print("Low Attendence")
    else:
        print("Very Low Attendence")
attendence = float(input("Enter attendence percentage"))
attendence_status(attendence)
'''
'''
# Customer Age group
# A marketing analyst wants to classify customers into age groups.
def age_group(age):
    if age < 18 :
        print("Teenager")
    elif age <30 :
        print("Young Adult")
    elif age <50 :
        print("Adult")
    else :
        print("Senior")
age = int(input("Enter Customer age: "))
age_group(age)
'''
'''
#Product Rating Analysis
# A company wants to analyze customer ratings for a product.
def rating_status(rating):
    if rating >= 4.5:
        print("Excellent Product")
    elif rating >= 3.5:
        print("Good Product")
    elif rating >= 2.5:
        print("Average Product")
    else:
        print("Poor Product")
rating = float(input("Enter product rating:"))
rating_status(rating)
'''
'''
#Data Quality Check
#A data analyst receives a customer age value and wants to check whether it is valid.
def check_age(age):
    if age<0 :
        print("Invalid age")
    elif age>100:
        print("Suspicious age")
    else:
        print("Valid age")
age = int(input("Enter customer age:"))
check_age(age)
'''
'''
#Missing Data check
# An analyst wants to check whether a customer email field contains data
def check_email(email):
    if email == "":
        print("Missing email")
    else:
        print("Email available")
email = input("Enter customer email: ")
check_email(email)
'''
'''
#Sales Target
#Create a function check_target(sales,target) that displays: "Target Achieved" if sales>=target
#"Target Not Achieved" otherwise
def check_target(sales,target):
    if sales>=target:
        print("Target Achieved")
    else:
        print("Target Not Achieved")
sales = int(input("Enter Sales: "))
target = int(input("Enter Target: "))
check_target(sales,target)
'''

#Custumer Purchase
# Create a function purchase_status: 






































