# a = 300
# b = 500
# if(a > b):
#     print("a is greater than b")
# elif(a < b):
#     print("a is smaller than b")
# else:
#     print("a is equal to b")


# short hand if : 

# if a == b : print("a is equal to b")


# short hand if .. else :

# print("a is greater than b") if a > b else print("a is equal to b")

# this technique is known as ternary operators, or conditional expressions : 

# print("a") if a > b else print(" = ") if a == b else print("b")


# and keyword is logical operator, and is used to combine conditional statements : 

# a = 200
# b = 33
# c = 400
# if a>b and c>b : 
#     print("both conditions are satisfied") 

# if a>b or c>b : 
#     print("at least one condition is satisfied") 


# the not keyword is a logical operator, and is used to reverse the result of the conditional statement : 
    
# if not b > a:
#     print("b is not greater than a")


# Nested if : 

# x = 19
# if x > 10:
#     print("above ten")
#     if x > 20:
#         print("above twenty")
#     else:
#         print("not above twenty")
    
# else:
#     print("not above ten")


# the pass statement : 

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

num1 = 100
num2 = 200
if num2 > num1:
    pass