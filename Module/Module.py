#----Module----- is a python file with .py extension 
#User define module
#creating a userdeffined module named bank.py having variable bal and 3 functions
bal=1000
def deposit(amount):
    bal=bal+amount
    return f"amount deposite, bal is {bal}"
def withdrawl(amount):
    bal=bal-amount
    return f"amount withdrawl, bal is {bal}"
def show_balance():
    return f"current bal is {bal}"

#save this file as bank.py

