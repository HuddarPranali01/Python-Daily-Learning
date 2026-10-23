#--------------Map function-------------
#map function in python applies a given function map return object to each item in an
#iterable (list)
'''
#syntax: map(function,iterable,.....)(no ke square denga)
res=lambda n:n*n
num=[1,2,3]
result=list(map(res,num))
print(result)
1
#ex: lambda function to add corresponding elements from two list
#(addition karenga dono list ke no ki like(1+4, 2+5, 3+6)
number1 = [1,2,3]
number2 = [4,5,6]
result = list(map(lambda x,y: x+y,number1, number2))
print(result)

#--------------FILTER FUNCTION--------------
#the filter() is use to filter elements from an iterable list
#ex: filter even no from iterable
num=[1,2,3,4,5,6,7,8]
result=list(filter(lambda x:x%2==0,num))
print(result)

#---------------SORTED FUNCTION------------------
#in python it is used to sort an iterable and return a new sorted list
#ex: sort even no from iterable
num=[11,2,3,4,15,6,7,8]
print(f"before sorting :{num}")
num.sort()
print(f"after sorting :{num}")

#ex:
numbers=[11,2,3,4,15,6,7,8]
sorted_numbers=sorted(numbers)
print(f"numbers: {numbers}")
print(f"after sorting : {sorted_numbers}")

#ex: reverse for ascending to descending order
numbers=[11,2,3,4,15,6,7,8]
sorted_numbers=sorted(numbers,reverse=True)
print(f"nnumbers:{numbers}")
print(f"after sorting : {sorted_numbers}")
'''
#ex:
words=["banana","apple","cherry"]
sorted_words=sorted(words)
print(sorted_words)



