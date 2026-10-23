'''
rno=(12,14,15)
print(type(rno))
print(rno)
'''
'''
#-----List[]-----
#list always follows indexing
#it is mutable,ordered collection it is slow. it has mixed datatype
my_list=[1,"apple",3.14,True]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
'''
'''
student=[123,"manisha","java"]
print("Student details")
print(f"roll number:{student[0]}")
print(f"name : {student[1]}")
print(f"course name : {student[2]}")
print("details using for loop")
for s in student:
    print(s)

#slicing - extract krna [start-end-step]
numbers=[0,1,2,3,4,5]
#slicing
print(numbers[1:4])
'''
'''
month=["jan","feb","mar","apr","may","jun"]
print(month[1:4])
print(month[0:5])
print(month[:3])
print(month[1:])
print(month[0:6:2])
print(month[::2])
print(month[4:1:-1]) #[4:1:-1]
'''
'''
#append(x): add an item x to the end of the list.list me last lena h
student=["manish","ravi","dilip"]
print(student)
name=input("Enter new student name")
#add this to list
student.append(name)
print('after adding new student')
print(student)
'''
















