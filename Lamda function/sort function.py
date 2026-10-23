'''
#sort the list with length of fruits using key in sorted method
words = ["banana","apple","cherry","kiwi","guava","pineapple"]
sorted_words = sorted(words, key = lambda x: len(x))
print(sorted_words)

#reverse
words = ["banana","apple","cherry","kiwi","guava","pineapple"]
sorted_words = sorted(words, key = lambda x: len(x),reverse=True)
print(sorted_words)

#sort a list of dictionary by a specific key
people = [{"name":"Alice","age":25},{"name":"Bob","age":30},{"name":"Charlie","age":20}]
sorted_people = sorted(people, key=lambda x:x["age"])
print(sorted_people)
'''
