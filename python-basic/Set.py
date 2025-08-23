# sets are used to store multiple items in a single variable.
# a set is a collection which is unordered, unchangeable*, and unindexed.

# note : set items are unchangeable, but we can remove items and add new items.

# sets are written with curly brackets.

set1={1,2,3,4,1}
print(set1)

# sets are unordered, so you cannot be sure in which order the items will appear.

# sets items are unordered, unchangeable, and do not allow duplicate values.

# unordered : set do not have defined order.
# it can not be referred to by index or key.

# sets are unchangeable : once set is created, we cannot change its items, but we can remove items and add new items.

# Duplicates are not allowed : 

print(set1)  # duplicate values will be ignored.

# True and 1 is considered the same value :
thisset = {1,True}
print(thisset)

# False and 0 are considered the same value in sets, and are treated as duplicates :
thisset2 = {0,False}
print(thisset2)

# get the length of a set : 

print(len(thisset2))
print(len(set1))

# set items-data types : 

# set items can be of any data types.
# A set contains different data types.

# type() : from python perspective, sets are defined as objects with the data type 'set' : 
print(type(set1))


# set() constructor : 

myset = set((1,2,3,4,5,6,7))
print(myset)


# access set items : 
# you cannot access items in a set by referring to an index or a key.

# but, we can use loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for x in myset:
    print(x,end = " ") 

print( 1 in myset)

# add items : 

# to add one item to a set use the add() method.
myset.add(100)
print(myset,end = " ")

# add sets : 
# to add items from another set into the current set, use the update() method.

set2 = {"1","a",20,"c"}
set3 = {1,2,3,"z"}

set2.update(set3)
print(set2)

# add any iterable : 

list1 = list(("5","6","7"))
set3.update(list1)
print(set3)


# remove set items : to remove an item in a set, use the remove(), or the discard() method. 
newset = {1,2,3,4,5}
# newset.remove(1)
newset.discard(1) # if the item to remove does not exist, discard() will not raise an error.
print(newset)


# pop() method : remove a random item by using the pop() method.
newset.pop()
print(newset)

# clear() method : empties the set : 
newset.clear()
print(newset)

# the del keyword will delete the set completely : 

# del newset
# print(newset)  # it will throw an error because newset is not defined.

# loop items : 
for x in set3:
    print(x,end=" ")

# join set : 

# there are several ways to join two or more sets in python : 

# we can use the union() method that return a new set containing all items from bith sets, or the update() methid that inserts all the items from one set into another : 
    
seta = {1,2,3,4,"a","b"}
setb = {"a","b","c",1,2,3}
# setc = seta.union(setb)

# seta.update(setb)
# print(seta)

# note : both union() and update() will exclude any duplicate items.

# keep only the duplicates : 

# seta.intersection_update(setb)
# print(seta)


# the intersection() method will return a new set, that only contains the items that are present in both sets.

# setc = seta.intersection(setb)
# print(setc)


# keep all but not the dupliacates : 

# seta.symmetric_difference_update(setb)
# print(seta)

# symmetric_difference will return a new set : 

# setc = seta.symmetric_difference(setb)
# print(setc)

# set methods : 
# add(), clear(), copy(), difference(), isdisjoint(), issubset(), issuperset(), pop(), remove(), union(), update(), symmetric_difference(), intersection_update() etc.




