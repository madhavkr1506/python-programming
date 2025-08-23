# lists are used to store multiple items in a single variable.
# lists are one of four built in data types in python used to store collections of data, the other three are tuple, set and dictionary, all with different qualities and usage.
# lists are created using square brackets :

thislist = [1,2,3,4,15,6,7,8,9,9,True,"Madhav"]
# print(thislist) 
# list items : 
# list items are ordered, changeable, and allow duplicate values.
# list items are indexed, the first item has index [0], the second item has index [1] etc.


# ordered : 
# when we say lists are ordered, it means that the items have a defined order, and that order will not change.

# if we add new items to a list, the new items will be placed at the end of the list.

# note : there are some list methods that will change the order, but in general: the order of the items will not change.

# changeable : 

# the list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# allow duplicates : 
# since lists are indexed, lists can have items with the same value : 

# list length : 
# print(len(thislist))

# list items data types : list can be of any data types.

# A list can contains different data types.

# type() : from python perspective, lists are defined as objects with the data type 'list : 
# print(type(thislist))

# the list() constructor : 
# it is possible to use the list() constructor when creating a new list.

mylist = list(("Mango","Madhav",True,1))
# print(mylist)

# python collections : 
# 1. List 2. Tuple 3. Set 4. Dictionary


# access item : 
# print(mylist[1])

# the first item has index 0.

# negative indexing : 

# negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

# print(mylist[-1])

# range of indexes : 
# print(mylist[0:2])

# the search will start from index 0 and end at index 2(not included).

# print(mylist[:1])

# print(mylist[1:])

# range of negative indexes

# print(thislist[-12:-4])

# check if item exists : 
#  to determine if a specified item is present in a list use the in keyword : 

# if("Madhav" in thislist):
#     print("Yes , it is in the list")
# else:
#     print("No , it is not in the list")

# Change list item : 

list1 = list(("a","b","c","d","e","a"))
# list1[1] = "1"
# print(list1)


# change the range of values : 
# list1[1:3] = ["1","2"]
# print(list1)

# list1[1:2] = ["a","b","c"] # if you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
# print(list1)   

# list1[1:4] = "a"
# print(list1)   # if you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.

# insert items : 
# the insert() method inserts an item at the specified index : 

# list1.insert(2,"Madhav")
# print(list1)


# append items : add an item to the end of the list
# list1.append("Madhav")
# print(list1)

# extend list : 
# to append elements from another list to the current list, use the extend() method.

# list2 = list(("1","2","3","4","5"))
# list1.extend(list2)
# print(list1)

# add any iterable : 

# tuple1 = ("Madhav","Krishna")
# list1.extend(tuple1)
# print(list1)



# remove specified item : 
# list1.remove("a")
# print(list1)

# list1.remove("1")  # it will through an error, as item x is not present in the list.
# print(list1)

# note : if there are more than one item with the specified value, the remove() method removes the first occurance : 

# list1.remove("a")
# print(list1)


# the pop() method : removed the specified index : 
# list1.pop(1)
# print(list1)

# if you do not specify the index, the pop() method removes the last item.
# list1.pop()
# print(list1)

# the del keyword also removes the specified index : 

# del list1[0]
# print(list1)

# the del keyword can also delete the list completely.

# del list1
# print(list1)


# clear the list : 
# the clear() method empties the list.

# the list still remains, but it has no content.

# list1.clear()
# print(list1)

# loop through a list : 

# for loop : 

# for x in list1 :
#     print(x,end=" ")


# loop through index numbers : 
# use the range() and len() function to create a suitable iterable : 
# for i in range(len(list1)):
#     print(list1[i],end = " ")

# using while loop : 

# i=0
# while i<len(list1):
#     print(list1[i],end = " ")
#     i = i + 1


# looping using list comprehension : 

# [print(x,end = " ") for x in list1]

# list comprehension :

# list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
 
# newlist1 = []
# for x in range(len(list1)):
#     newlist1.append(list1[x])

# print(newlist1)

# newlist = [print(list1[x],end = " ") for x in range(len(list1))]
# print(newlist)

# the syntax : newlist = [expression for item in iterable if condition == True]

list2 = ["Apple","Mango","Banana","Orange","Grapes"]
# newlist2 = [x for x in list2 if x != "Apple"]
# print(newlist2)


# with no if statements : 

# newlist2 = [x for x in list2]
# print(newlist2)


# use range() function

# newlist2 = [x for x in range(10)]
# print(newlist2)

# newlist2 = [print(list2[x]) for x in range(len(list2))]

# newlist2 = [x for x in range(10) if x < 5]
# print(newlist2)

# newlist2 = [x.upper() for x in list2]
# print(newlist2)

# newlist2 = ["Apple" for x in list2]  # set all values in the new list to "Apple"
# print(newlist2)

# newlist2 = [x if x != "Apple" else "Orange" for x in list2] # return the item if it is not Apple, if it is Apple return Orange.
# print(newlist2) 

# sort() method that will sort the list alphanumerically, ascending, by default :  

# list2.sort()
# print(list2)

# sort in descending order
# list2.sort(reverse=True)
# print(list2)

# customize sort function : 

# we can also customise our own function by using the keyword argument key = function.

# def myfun(n):
#     return abs(n-50)
# list3 = [100,50,65,82,23]
# list3.sort(key = myfun)
# print(list3)

# case insensitive sort : 

list4 = ["Orange","mango","Zebra","parrot","apple"]
# list4.sort()
# print(list4)

# list4.sort(key = str.lower)
# we can use built in functions as key functions when sorting a list.
# so if you want a case insensitive sort function, use str.lower as a key function.


# list4.sort(key = str.lower)
# print(list4)


# reverse order : 
# the reverse() method reverses the current sorting order of the elements.

# list4.reverse()
# print(list4)

# copy a list : 

# there a way to make a copy, one way is to use the built in list method copy().

# list5 = list4.copy()
# print(list5)

# join two list : 

# by using + operator

list6 = ["a","b","c"]
list7 = [1,2,3]

# list8 = list6 + list7
# print(list8)

# using extend() : 
# list6.extend(list7)
# print(list6)


# using append() : 
# for x in list7:
#     list6.append(x)

# print(list6)

# list methods : 
# append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()


























