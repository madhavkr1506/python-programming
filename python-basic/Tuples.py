# tup;es are used to store multiple items ina single variable.
# tuple is a  collection which is ordered and unchangeable.
# tuples are written with round brackets.

tuple1 = ("Madhav","Kumar","Madhav")
print(tuple1)

# tuple items are ordered, unchangeable, and allow duplicate values.
# tuple items are indexed, the first item has index 0.

# ordered : tuple items have a defined order, and that order will not change.

# unchangeable : we can not add or remove items after the tuple has been created.

# allow duplicates : since tuple are indexed, they can have items with the same value : 


# tuple length : 
print(len(tuple1))

# creating tuple with one item : 
tuple2 = ("Madhav",)
print(type(tuple2)) # one item tuple, remember the comma: 

tuple3 = ("Madhav")
print(type(tuple3))  # it is not a tuple, it is a string.

# tuple items - data types : 

# tuple items can be of any data type : 

# A tuple can contain different data types.

tuple4 = ("a",1,True)
print(tuple4)

# type()  : from python perspective, tuples are defined as objects with the data types 'tuple':
print(type(tuple4))

# the tuple() constructor : 

tuple5 = tuple(("1","2","3"))
print(tuple5)

# access tuple items : 
print(tuple5[1])

# negative indexing : 
print(tuple5[-1])

# range of indexes : 
print(tuple5[0:2])

print(tuple5[:2])
print(tuple5[1:])

# range of negative indexing : 

print(tuple5[-3:-1])

# check if item exists : 
# to determine if a specified item is present in a tuple use the in keyword : 
tuple6 = tuple((1,2,3,4,5,6,7,8))
if(1 in tuple6):
    print("Yes it is present in the tuple6")
else:
    print("No it is not present the tuple")

# update tuples : 
    
# tuples are unchangeable, meaning that we can not change, add, or modify or remove items once tuple is created.
# but there are some workarounds.

# convert tuple into a list to be able to change it : 
    
tuple7 = ("a","b","c")
list1 = list(tuple7)
list1[1] = "Z"
tuple7 = tuple(list1)
print(tuple7)

# add items : 

# 1. convert it into list : 

tuple8 = tuple((1,2,3,4))
list2 = list(tuple8)
list2.append(5)
tuple8 = tuple(list2)
print(tuple8)

# 2. add tuple to a tuple : 
tuple9 = (1,2,3)
tuple10 = (4,)
tuple9 += tuple10
print(tuple9)

# remove items : 
tuple11 = (1,2,3,4,5)
list3 = list(tuple11)
list3.remove(5)
tuple11 = tuple(list3)
print(tuple11)


# delete tuple completely : del keyword

# del tuple11
# print(tuple11)   # this will throw an error because the tuple no longer.

# unpack tuples : 

# packing a tuple : 
tuple12 = (1,2,3,4,5)

# but in python, we are also allowed to extract the values back into variables. this is called unpacking :

tuple13 = ("1","2","3")
(one,two,three) = tuple13

print(one)
print(two)
print(three)

# The number of variables muct match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# using asterisk * : 
# if the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list : 

tuple14 = ("one","two","three","four")
(one,*two) = tuple14
print(one)
print(two)

# if the asterisk is added to another variable name than the last, python will assign values to the variable until the number of values left matches the number of variable left.

tuple15 = ("one","two","three","four")
(one,*two,three) = tuple14
print(one)
print(two)
print(three)

# loop in tuple  

# for loop : 
for x in tuple15:
    print(x)

for i in range(len(tuple15)):
    print(tuple15[i])

# while loop : 

i = 0
while i < len(tuple15):
    print(tuple15[i],end=" ")
    i = i + 1

# join two tuple : 
tuple16 = (1,2,3,4)
tuple17 = (5,6,7,8)
tuple18 = tuple16 + tuple17
print(tuple18)

# multiply tuple : 
print(tuple18 * 2)

# tuple methods : 
# count(), index()