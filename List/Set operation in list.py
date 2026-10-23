#Tuple- immutable ordered collection()
#List-mutable ordered collection with duplicate item []
#Set- mutable unordered collection with unique item {}
# A set in Python is a mutable, unordered collection of unique, immutable element for storing
#distinct items
'''
#Creating set
# stud={111,"prana","java","prana"}
# print(stud)

#using set constructor
stud={111,"prana","java","prana"}
print(stud)
'''
'''
#union
stud1={"amit","atul"}
stud2={"sneha","nita"}
stud3={"dhruvi","krisha"}
stud=stud1 | stud2 | stud3
print("all student")
print(stud)
'''
'''
#intersection-(common lena h to ye use kre)
stud1={"amit","atul"}
stud2={"atul","nita"}
stud=stud1 & stud2
print("common student")
print(stud)
'''
'''
#Difference-
stud1={"amit","atul","manisha","mona"}
stud2={"atul","amit"}
stud=stud1 - stud2
print("difference in student")
print(stud)

days={"mon","tue","wed","thurs","fri","sat"}
attendance={"tue","thurs","fri"}
absent= days - attendance
print("employee absent on:")
print(absent)
'''
'''
#symmetric diffrence-
days={"mon","tue","wed","thurs","fri","sat"}
attendance={"tue","thurs","fri","sun"}
absent= days ^ attendance
print("symmetric difference:")
print(absent)
'''
'''
#Subset and Superset
course1 = {"java","php","python","oracle","html"}
course2 = {"php","html"}
result = course2<=course1  #subset
print(result)

result=course1>=course1  #superset
print(result)
'''
'''
#add- Adds an element x to the set

#remove-
course = {"java","php","html"}
c = input("Enter course name to remove")
course.remove(c)
print("course removed from set")
print("course available")
print(course)
'''
'''
#discard- removes element
course = {"java","php","html","oracle"}
c = input("Enter course name to discard")
course.discard(c)
print("course discard from set")
print("course available")
print(course)
'''
#pop-removes and return an arbitary element
#clear









