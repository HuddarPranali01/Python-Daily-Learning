'''
MATCH Statement(similar to switch)
The match statement in Python provides a switch -case-like syntax for structural pattern matching
Syntax :
match expression :
  case pattern 1:
    #Code block for pattern 1
  case pattern 2 :
    #Code block for pattern2
 case _:
 '''
'''
# accept dayno and print dayname using match satement
dayno = int(input("Enter dayno(1-7)"))
match dayno :
    case 1 :
        print("Monday")
    case 2 :
        print("Tuesday")
    case 3 :
        print("Wednesday")
    case 4 :
        print("Thursday")
    case 5 :
        print("Friday")
    case 6 :
        print("Saturday")
    case 7 :
        print("Sunday")
    case _ :
        print("Some other day")
'''

'''
monthno = int(input("Enter monthno(1-12)"))
match monthno :
    case 1 :
     print("January")
    case 2 :
     print("February")
    case 3 :
     print("March")
    case 4 :
     print("April")
    case 5 :
     print("May")
    case 6 :
     print("June")
    case 7 :
     print("July")
    case 8 :
     print("August")
    case 9 :
     print("September")
    case 10 :
     print("October")
    case 11 :
     print("November")
    case 12 :
     print("December")
    case _:
     print("Default")
'''


#accept 2 numbers and operator and print result using match
n1 = int(input("Enter number 1"))
n2 = int(input("Enter number 2"))
op = input("Enter operator +,-,*,/")
match op :
    case '+' :
        result = n1+n2
    case '-' :
        result = n1-n2
    case '*' :
        result = n1*n2
    case '/' :
        result = n1/n2
    case _:
        print("Not a valid Operator")
print(f"result : {result}")


'''
#accept score and print grade
score = int(input("Enter Score"))
match score :
    case p if p>=90 and p<=100 :
        print("Grade A")
    case p if p>=80 :
        print("Grade B")
    case p if p>=70 :
        print("Grade C")
    case p if p>=0 :
        print("Grade Fail")
    case _:
        print("Invalid Score")
'''

#Default case (wildcard) for unmatched patterns

'''
#program to accept traffic color light and print either go,stop, ready
color = input("Enter traffic light color: ")
match color :
  case "Green":
    print("You can go")
  case "Red" :
    print(" Plaese Stop")
  case "Yellow" :
    print("Ready to go")
  case _:
    print("Invalid color")
'''

'''
#prgram to accept age and print whether old, young or child
age = int(input("Enter Age: "))
match age :
    case _ if age>=45 :
        print("OLD")
    case _ if age>=16 :
        print("YOUNG")
    case _ if age>=0 :
        print("CHILD")
    case _:
        print("Invalid Age")
'''

#program to accept sales_amount and print whether eligible to discount or not
sales=int(input("Enter current sales :"))
match sales:
    case a if sales<=10 :
        print("40% Discount")
    case a if sales<=30 :
        print("25% Discount")
    case a if sales<=100 :
        print("10% Discount")
    case _:
        print("No Discount")
#accept character and print vowel or not
# ch = input("Enter Character :")
# match ch :
#     case 'a'|'e'|'i'|'o'|'u' :
#      print("Vowel")
#     case _:
#      print("Not a Vowel")
#     










