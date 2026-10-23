#------Lamda functions-----

'''
add= lambda x,y : x+y
print(add(2,3))

sub=lambda a,b:a-b
print(sub(5,2))

mul=lambda x,y:x*y
n1=int(input("Enter number1"))
n2=int(input("Enter number2"))
result=mul(n1,n2)
print(f"multiplication :{result}")

#square of a number
sq=lambda x:x**2  #x*x
n=int(input("Enter number"))
result=sq(n)
print(f"square of a number :{result}")

#concatinate 2 strings
fullname=lambda fn,ln :fn +" " +ln #" " is used for space
print(fullname("Laranya","Huddar"))

#Even odd
result=lambda x :x%2==0  #true/false
print(result(6))

#greater of 2 numbers
result = lambda x,y : x if x>y else y
print(f"greater number is : {result(5,40)}")

#calculate length of string
l=lambda s : len(s)
print("length", l("Pranali Huddar"))

#positive or negative
result = lambda n : "Positive" if n>0 else "Negative"
print(result(-4))
'''



















