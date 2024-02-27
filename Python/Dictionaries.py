# pyhton dictionaries : 
# it is used to store data values in key:value pairs.
# a dictionary is a collection which is ordered*, changeable, and do not allow duplicates.


# dictionaries are written with curly brackets, and have key and values : 

dict1 = {"a":1,"b":2,"c":3}
print(dict1)

print(dict1["a"]) # dictionary items can be referred by using the key name.

# as of python version 3.7, dictionaries are ordered. in python 3.6 and earlier, dictionaries are unordered.
# ordered means : items have a defined order, and that order will not change.
# unordered means : items do not have a defined order, you cannot refer to an item by using an index.

# changeable : dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# duplicates not allowed : 
# we cannot have two items with the same key.

dict2 = {"a":1,"b":2,"c":3,"c":4}
print(dict2)

# dictionary length : 

print(len(dict2))

# dictionary items data types : 
# the values in dictionary items can be of any data type.

# type()

# from python perspective, dictionaries are defined as objects with the data type 'dict'.
print(type(dict2))

# the dict() constructor : 
dict3 = dict(name = "Madhav",regNo = 12213356,Gender = "Male")
print(dict3)


# access dictionary items : 
print(dict3["name"])

# there is also a method called get() that will give you the same result : 
print(dict3.get("name")) 

# get keys() : the keys() method will return a list of all the keys in the dictionary.

print(dict3.keys())

# add a new item to the original dictionary : 

dict3["mobile"] = 123456
print(dict3)

# get values() : return a list of all the values in the dictionary.
val = dict3.values()
print(val)


# make a change in original dictionary : 

dict3["name"] = "Krishna"

print(dict3)


# get items : 
# return each item in a dictionary, as tuples in a list.

items = dict3.items()
print(items)

# check if key exists : 

if "name" in dict3 : 
    print("yes it is in dict3")
else:
    print("no it is not in dict3")

# we can change values : 
dict3["name"] = "Gopal"
print(dict3)

# we can update : 
dict3.update({"name":"Madhav"})
print(dict3)

# the update() method will update the dictionary with the items from the given argument.


# removing items : 

# the pop() method removes the item with the specified key name : 
# dict3.pop("mobile")
# print(dict3)


# popitem() method removes the last inserted item(in version before 3.7, a random item is removed instead).
# dict3.popitem()
# print(dict3)


# the clear() method empties the dictionaries : 

# dict3.clear()
# print(dict3)

# the del keyword removes the item with the specified key name : 

# del dict3["Gender"]
# print(dict3)

# the del keyword delete the dictioanry completely : 

# del dict3
# print(dict3) # it will throw an error because dict3 is not defined.

# loop through a dictionary : 

# print all key names in the dictionary, one by one : 

for x in dict3:
    print(x)

# print all values in the dictionary, one by one : 

for x in dict3:
    print(dict3[x])

# values() method to return values of a dictionary : 
for x in dict3.values():
    print(x)

# keys() method to return all the keys of a dictionary : 
for x in dict3.keys():
    print(x)

# loop through both keys and values, by using the items() method : 
    
for x , y in dict3.items():
    print(x,y)


# copy dictionaries : 

# copy() method : 

dict4 = dict3.copy()
print(dict4)

# another way to make a copy of a dictionary with the dict() function : 
dict5 = dict(dict3)
print(dict5)


# nested dictionaries : 
# create dictionary that contain three dictionaries : 

dictall = {"dict1":{"name" : "Madhav","Reg no":12213356},"dict2":{"name" : "Krishna","Reg no":12213357},"dict3":{"name" : "Raghav","Reg no":12213358}}
print(dictall)


# access nested dictionary : 

print(dictall["dict2"]["Reg no"])

# python dictionary method : 
# clear(), copy(), fromkeys(), get(), items(), values(), keys(), pop(), popitem(), setdefault(), update() etc.
