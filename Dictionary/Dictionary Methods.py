'''
#dictionary to store current user (id,name,role)
current_user={"id":123,"name":"manisha","role":{"admin","customer"}}
print(current_user)
print("current user details")
print(f"id:{current_user['id']}")
print(f"name:{current_user['name']}")
print(f"role:{current_user['role']}")
'''
'''
current_user={"id":123,"name":"manisha","role":{"admin","customer"}}
print(current_user)
print("current user details")
print(f"id:{current_user['id']}")
print(f"name:{current_user['name']}")
r=current_user['role']   #set
r1=list(r) #converting set to list
print(f"role 1:{r1[0]}")
print(f"role 2:{r1[1]}")
'''
'''
#----Dictionary Methods----
#keys
current_user={"id":123,"name":"manisha","role":{"admin","customer"}}
print("keys",current_user.keys())
#values
print("values",current_user.values())
#items
print("items",current_user.items())
#get
print("get",current_user.get("id1",706))
'''
'''
#pop item-last me jo rehta h vhi pop me aata
patient={"id":111,"name":"ravi","doctname":"mahesh"}
print(patient)
p1=patient.popitem() #return last key value and remove it from dict.
print("pop item " ,p1)
print('remaining ' ,patient)
'''
'''
patient={"id":111,"name":"ravi","doctname":"mahesh"}
print(patient)
p1= {"doctname":"sanskar","mobile":9898769882}
patient.update(p1)
print(patient)
'''
'''
patient={}
#adding a new key value pair to dictionary
pid=int(input("enter patient id"))
patient["id"]=pid
pn=input("enter patient name")
patient["name"]=pn
# display the patients
print("patient details")
print(patient)
id=input("enter key to update")
val=input("enter value")
patient.update({id:val})
print(patient)
'''
'''
tempadd={"area":"sadar","city":"nagpur"}
permadd=tempadd.copy() #create a duplicate copy of dictionary
print(permadd)
'''
stud={}
for i in range(3):
    name=input("enter name")
    math=int(input("enter maths"))
    chem=int(input("enter chem"))
    stud[name]={"math":math,"chem":chem}
print(stud)
             




