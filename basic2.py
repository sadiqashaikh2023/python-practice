# dictionary in python
# mapped data:dict 
# dict is a collection of key value pair
dict1 = {"id":1,"name":"sadiqa","age":30,"canvote":"true"}
print(dict1)
dic = {"name": "yahya", "age": 2, "colour": "fair", "hobby": "crying"}
print(dic["name"]) # if not found show error
print(dic.get("name")) # if not found show (none)

# accessing multiple values
print(dic.values())

# accessing multiple keys
print(dic.keys())

# using for loop to get key and value
for key in dic.keys():
    print(dic[key])

# using f string with for loop
for key in dic.keys():
    print(f"value of corresponding key {key} is {dic[key]}")

# accessing key
print(dic.items()) # show all the items in dic(key and value both)
for key, value in dic.items():
    print(f"value of corresponding key {key} is {value}")

# dictonary methods
e1 = {122:50,167:45,110:70,123:34}  #to add value
e2 = {156:89,133:78,457:67}
e1.update(e2)
print(e1)      

# #remove items from dictonary
# e1.clear()
# print(e1)

 ## to make empty dictnory
emp = {}
print(emp)  

## pop method taks key and remove key with value
e1.pop(156)
print(e1)

## pop item remove last key value
e1.popitem()
print(e1)

## del delete the dictnory
del e2
# print(e2) # show error

del e1[122]
print(e1)