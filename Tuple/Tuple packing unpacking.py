'''
def process(a,b):
    a1,a2=a    #unpacking the tuple
    b1,b2=b    #unpacking
    a1="abc1"
    a2="abc2"
    b1=0.1
    b2=0.2
    return (a1,a2),(b1,b2)
a=("abc","bbc")
b=(0.0,0.0)
a,b=process(a,b) #pass a and b tuple to function process
for i in a:
    print(i)
for j in b:
    print(j)
'''
'''
# A list in python is a mutable, ordered collection of items that can store elements of different
#data types.

#creating a empty list
stud = []
print(stud,type(stud))
student=[123,"Amit","amit@gmail.com", 1233455678]
print(student)
print('student details')
print(f"roll number : {student[0]}")
print(f"name:{student[1]}")
print(f"email : {student[2]}")
print(f"mobile nno. :{student[3]}")
'''
'''
#Similarly accept rno,email and mobile from user, and store it in a list and the display
#the studnets details.
rno=int(input("enter rno"))
name=input("enter name")
email=input("enter email")
mobile=input("enter mobile number")
student=[rno,name,email,mobile]
print(student)
print('student details')
print(f"student roll number:{student[0]}")
print(f"student name:{student[1]}")
print(f"student email:{student[2]}")
print(f"student mobile:{student[3]}")
'''

'''
#accept empno,name,salary and designation of employee and store it in a list and then print the
#employee details from list
empno=int(input("Enter Empno"))
empname=input("Enter empname")
salary=input("Enter salary")
designation=input("enter designation")
employee=[empno,empname,salary,designation]
print(employee)
print('employee details')
print(f"employee number:{employee[0]}")
print(f"employee name:{employee[1]}")
print(f"employee salary:{employee[2]}")
print(f"employee designation:{employee[3]}")
'''







