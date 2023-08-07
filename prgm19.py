#string methods

string = "Hello, World!"

lenght = len(string)
print("lenght of string:",lenght)

uppercase = string.upper()
print("Uppercase string:",uppercase)

lowercase = string.lower()
print("Lowercase string:",lowercase)

count = string.count("o")
print("no of 'o' in string :",count)

#list methods

list = [1,2,3,4,5]

lenght = len(list)
print("lenght of list:",lenght)

list.append(6)
print("list after appending element:",list)

list.sort()
print("sorted list:",list)

list.reverse()
print("reversed list:",list)

#dictonary methods

dict = {"name":"john", "age":26,"city":"gadag"}

lenght = len(dict)
print("Length of dict :",lenght)

keys = dict.keys()
print("keys in a dict:", keys)

values = dict.values()
print("Values of dict is:", values)

key_exists = "age" in dict
print("does 'age' exist in dict:",key_exists)

dict.pop("age")
print("dictionary after removing age:",dict)
