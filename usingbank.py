'''
#----Modules----
#Module is a python file which contains functions,classes and variables
#which can be reused in any python program
#Types of modules
#1-Builtin module->math,random,os
#2-Third party module->pandas,numpy,scikit_learn,pytorch
#3-User defined module->(custom module)
'''
'''
#1-Builyin module
import math #math is builtin module
print(math.pi)
print(math.sqrt(20))
print(math.cos(0))

from math import pi,sqrt #another way to import module
print(pi)
print(sqrt(20))

from math import sqrt as s,pi as p #shortcut -alias
print(p)
print(s(16))

import random 
print(random.randint(1,10))
'''
#user defined module
def deposit(amount):
    bal=1000
    bal=bal+amount
    return f'amount deposited,bal is{bal}'















