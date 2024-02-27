# python for loops : 

# it  is used for iterating over a sequence( that is either a list, a tuple, a dictionary, a set, or a string).

list1 = list(("Madhav","Krishna","Mohan","Mohit","Rahul","Rohit"))
# for x in list1:
#     print(x)


# looping through string : 

# for x in "Madhav":
#     print(x)

# the break statement : 

# for x in list1:
#     if x == "Krishna":
#         break
#     print(x)

# the continue statement : 

# for x in list1:
#     if x == "Mohan":
#         continue
#     print(x)

# the range() function : 

# for x in range(len(list1)):
#     print(list1[x])


# using start parameter : 

# for x in range(1,4):
#     print(list1[x])

# increment sequence by 2 : 

# for x in range(1,4,2):
#     print(list1[x])

# else in for loop : 

# for x in range(10):
#     print(x)
# else:
#     print("finally fininshed!")

# the else block will not be executed if the loop is stopped by a break statement.

# for x in range(10):
#     if(x == 5):
#         break
#     print(x)
# else:
#     print("finally fininshed!")


# nested loops : 

# a nested loop is a loop inside a loop
# the inner loop will be executed one time for each iteration of outer loop : 

# a = ["a","b","c","d","e"]
# b = [1,2,3,4,5]
# for x in a:
#     for y in b:
#         print(x,y)


# the pass statement : 

for x in [0,1,2,3]:
    pass

# for loops cannot be empty , but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.


