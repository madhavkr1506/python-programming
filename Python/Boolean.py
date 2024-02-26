# boolean represent one of two values : true or false

# print(10 > 8)
# print(8 > 10)
# print(10 == 8)

# when you run condition in an if statement, python returns true or false
# a = 100
# b = 50
# if(a > b):
#     print(a,"greater than ",b)
# else:
#     print(a," is smaller than ",b)


# evaluate values and variables : 

# print(bool("Madhav"))  # it will give true
# print(bool(10)) # it will give true
# print(bool(0)) # it will give false

# most values are true : 
# almost any values is evaluated to true if it has some sort of content.
# any string is true, except empty strings.
# any number is true, except 0.
# any list, tuple, set and dictionary are true, except empty ones.


# the following will return false : 

# print(bool(False))
# print(bool(""))
# print(bool(0))
# print(bool(None))
# print(bool(()))
# print(bool([]))
# print(bool({}))


# one more value, or object in this case, evaluates to false, and that is if you have an object that is made from a class with a _len_ function that returns 0 or false :

# class myclass():
#     def __len__(self):
#         return 0
    
# myobj = myclass()
# print(bool(myobj))

# functions can return boolean value : 

# def myfunction():
#     return True
# print(myfunction())

# def function1():
#     return True
# if(function1()):
#     print("Yes true")
# else:
#     print("no false")


# python also has many built in function that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type : 
x = "Madhav"
print(isinstance(x,str))

