'''
#program to accept names
names=[]  #empty list
print("Select your choice")
print("1-add student name")
print("2-Exit")
while(True):
    choice=int(input("Enter choice"))
    if choice==1:
        n=input("Enter student name")
        names.append(n)
    elif choice==2:
        break
print("list of students added")
print(names)
'''
'''
#wap accept roll number, name n course
names=[]  #empty list
print("Select your choice")
print("1-add student name")
print("2-Exit")
while(True):
    choice=int(input("Enter choice"))
    if choice==1:
        r=int(input("Enter roll number"))
        n=input("Enter student name")
        c=input("Enter course")
        stud=(r,n,c)
        names.append(stud)
    elif choice==2:
        break
print("list of students details")
for i in names:
    print(f"roll no :{i[0]}")
    print(f"name :{i[1]}")
    print(f"course : {i[2]}")
'''

