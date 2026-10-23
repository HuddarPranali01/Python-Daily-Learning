'''
What is JSON?
JSON (JavaScript Object Notation)


#json.dumps()     file -> object
import json
#Creating a dictionary object to store payment details
payment={"id":1,"cust_name":"pranali","amount":120.20}
#creating python dictionary object to json object
jp = json.dumps(payment,indent=4)   #space indentation 4
print("json payment details")
print(jp)


#json.dump()   Object -> file
import json
#Creating a dictionary object to store payment details
payment={"id":1,"cust_name":"pranali","amount":120.20}
#creating python dictionary object to json file
with open('payment.json','w') as file:
   json.dump(payment,file)   
print("json file created")
'''

#json.loads()  String->Object       (load is used to convert json file into python dictionary
#object)
import json
with open('payment.json','r') as file:
    result=json.load(file)
print(result)

