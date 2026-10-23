#while Loop : Executes as long as a condition is True
#It is used when the number of iterations
'''
#wap to print no. from 1 to 5 using while loop
i=1
while i<=5 :
    print(i)
    i +=1
'''
#5 to 1
i=5
while i>=1 :
    print(i)
    i -=1
'''
# 21 to 30
i=21
while i<=30 :
    print(i)
    i += 1
'''

# i=1
# while True:
#     print(i)
#     i += 1
#     if i>10 :
#         break
# print("bye")

'''
#wap to accept a number and print factorial
while True :
     num=int(input("Enter number"))
     fact=1
     while num>0 :
         fact=fact * num
         num -= 1
     print(f"fact : {fact}")
     ans=input("Do you want to continue , press yes or no").lower()
     if ans=="no" :
         break
print("bye")
'''
#wap to accept password
password=input("Enter password")#Abc@123
isdigit=False
isspecial=False
special="!@#$%"
if len(password) >= 8 :
    for p in password:
        if p.isdigit():
            isdigit=True
        elif p in special :
            isspecial=True
    if isdigit==True and isspecial==True:
        print("Password is Valid")
    else:
        print("Invalid Password")
else:
    print("Password should be atleast 8 characters")















