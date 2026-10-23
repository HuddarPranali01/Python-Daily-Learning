#CSV File handling
#it helps u read from write to csv(comma
'''
#program to create a csv file and write the data into it
#Example1
import csv
#create or open the csv file in write mode
with open('student.csv','w',newline='') as file:
    w=csv.writer(file)
    w.writerow(['Name','Age','Salary'])
    w.writerows([['Pranali',20,60000],['Nidhi',19,50000]])
print("csv file created successfully")

#Example2
import csv
with open('student.csv','w',newline='')as file:
    w=csv.writer(file)
    w.writerow(['Name','Age','Salary'])
    for i in range(3):
    n=input("Enter name")
    a=int(input("Enter age"))
    s=float(input("Enter Salary"])
    w.writerows([[n,a,s]])
print("csv file created successfully")

'''
# Example of csv.apend()-a 'w'chya jaagi a
import csv
with open('student1.csv','a',newline='')as file:
    w=csv.writer(file)
    w.writerow(['Name','Age'])
    w.writerows([['amit',20],['ravi',30]])
print("csv file created successfully")


    
'''
#-----csv.reader()- used to READ data from csv file
import csv
with open('student.csv','r',newline='')as file:
    read=csv.reader(file)
    print("student details")
    
    for r in read:
        print(type(r))
        print(r)
    
    print("----Student details------")
    for r in read:
        print(f"name :{r[0]},age:{r[1]}, salary:{r[2]}")
 '''
'''
#Example of read
import csv
with open('student1.csv','r',newline='')as file:
    w=csv.reader(file)
    next(w)  #skip the first row
    for r in w:
        print(r)
'''

