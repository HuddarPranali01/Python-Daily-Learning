'''
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
search_roll=int(input("Enter roll number to search:"))
found=False
for i in names:
    if i[0]==search_roll:
        print(f"Found!Roll No:{i[0]}|Name:{i[1]}|Course:{i[2]}")
        found=True
        break
if not found:
    print("Student not found")
    '''
#Program to manage student records
names = [] #empty list to store student tuples

while True:
    print("\n---SELECT YOUR CHOICE---")
    print("1-Add student details")
    print("2-Display all students---")
        
        
#assignment to do list program
    
        
        