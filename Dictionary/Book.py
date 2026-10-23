'''
#create a class book
class Book:
    title = None
    author = None
    price = 0
b = Book()
print("enter book details")
b.title=input("enter title")
b.author=input("enter author")
b.price=int(input("enter price"))
print("book details")
print(f"title:{b.title}")
print(f"auther:{b.author}")
print(f"price:{b.price}")
'''
#create a class customer having attributes
#cust_id,cust_namme,cust_email,cust_mobile

#create a class patient having attr.pat_id,name,disease,doctor name