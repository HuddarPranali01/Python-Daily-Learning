#Exception handling
#Keyword->try,except,else,finally,raise statements
'''
#accept bill details
cust_name=input("Enter your name")
amount=float(input("Enter bill amount"))

print("--------details-----")
print(f"Customer name :{cust_name}")
print(f"bill amount:{amount}")
print("------Thank you-----")
#If enter bill amount=acsd then error found
try:
    cust_name=input("Enter your name")
    amount=float(input("Enter bill amount"))
except ValueError as e:  #this block will execute if exception occurs
    print(f"error : {e}")
    amount=float(input("Enter bill amount"))
except Exception as e:
    print(f"error : {e}")
print("--------details-----")
print(f"Customer name :{cust_name}")
print(f"bill amount:{amount}")
print("------Thank you-----")

# Example of try,except and else
try:
    cust_name=input("Enter your name")
    amount=float(input("Enter bill amount"))
except ValueError as e:  #this block will execute if exception occurs
    print(f"error : {e}")
    amount=float(input("Enter bill amount"))
except Exception as e:
    print(f"error : {e}")
else:
    print("--------details-----")
    print(f"Customer name :{cust_name}")
    print(f"bill amount:{amount}")
print("------Thank you-----")
'''
'''
#Example of try,except,else n finally block
try:
    cust_name=input("Enter your name")
    amount=float(input("Enter bill amount"))
except ValueError as e:  #this block will execute if exception occurs
    print(f"error : {e}")
    amount=float(input("Enter bill amount"))
except Exception as e:
    print(f"error : {e}")
else:
    print("--------details-----")
    print(f"Customer name :{cust_name}")
    print(f"bill amount:{amount}")
print("------Thank you-----")

#Example of try,except,else and finally
try:
    cust_name=input("Enter your name")
    amount=float(input("Enter bill amount"))
except ValueError as e:  #this block will execute if exception occurs
    print(f"error : {e}")
    amount=float(input("Enter bill amount"))
except Exception as e:
    print(f"error : {e}")
else:    #will execute if execution does not occur
    print("--------details-----")
    print(f"Customer name :{cust_name}")
    print(f"bill amount:{amount}")
finally:
    print("------Thank you-----")
'''
'''
#Using discount
try:
    cust_name=input("Enter your name")
    amount=float(input("Enter bill amount"))
    discount="20" #str
    amount=amount - discount
except ValueError as e:  #this block will execute if exception occurs
    print(f"error : {e}")
except Exception as e:
    print(f"error : {e}")
    amount=amount - float(discount)
else:    #will execute if execution does not occur
    print("else block")
finally:
    print("--------details-----")
    print(f"Customer name :{cust_name}")
    print(f"bill amount:{amount}")
    print("------Thank you-----")
'''
#Example of raise
try:
    cust_name=input("Enter your name")
    amount=float(input("Enter bill amount"))
    if amount<0:
        raise Exception("amount cannot be less than zero")
except ValueError as e:  #this block will execute if exception occurs
    print(f"error : {e}")
except Exception as e:
    print(f"error : {e}")
    amount=float(input("Enter bill amount"))
else:    #will execute if execution does not occur
    print("else block")
finally:
    print("--------details-----")
    print(f"Customer name :{cust_name}")
    print(f"bill amount:{amount}")
    print("------Thank you-----")





















