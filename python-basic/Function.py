# a function is a block of code which only runs when it is called.

# you can pass data, known as parameters, into a function.

# a function can return data as a result.

# def function1():
#     print("My name is madhav")

# to call a function, use the function name followed by parenthesis : 

# function1()


# arguments : 
# information can be passsed into functions as arguments : 
# arguments are specified after the function name, inside the parentheses. we can add as many arguments as we want, just separate them with a comma.

# def myname(name):
#     print(name + " Hello")

# myname("Madhav")


# arguments are often shortened to args in python documentations.

# parameters or arguments ?

# these terms can be used for the same thing : information that are passed into a function.

# from a function's perspective  : 


# a parameter is the variable listed inside the parentheses in the function definition.
# an argument is the value that is sent to the function when it is called.
# number of arguments : by default, a function must be called with the correct number of arguments.


# def fullname(name,surname):
#     print(name," ",surname)

# fullname("Madhav","Kumar")

# arbitrary arguments, *args

# if you dont know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# this way the function will receive a tuple of arguments, and can access  the items accordingly.

# def friend(*name):
#     print("Names listed : " + name[0])

# friend("Madhav","Krishna","Raghav","Raghu")

# keyword arguments : 

# we can also send arguments with the key = value syntax.

#  in this way the order of the arguments does not matter.

# def function1(name1,name2,name3):
#     print("Name is "+name3)

# function1(name3 = "Madhav",name2 = "Krishna",name1 = "Ganesh")


# arbitrary keyword arguments, **kwargs : 

# if you do not know how many keyword arguments that will be passed into your function, add two asterisk : ** before the parameter name in the function definition.

# def function2(**name):
#     print("My name is "+name["fname"]) 
# function2(fname = "Madhav",lname = "Kumar")

# default parameter value : 

# def function1(country = "India"):
#     print("I am from : "+country)

# function1()
# function1("Korea")


# passing a list of arguments : 

# passing a list as an arguments : we can send any data types of arguments to a function(string, number, list, dictionary etc.), and it eill be treated as the same data type inside the function.

# def function1(places):
#     for x in places:
#         print(x)


# list1 = list(("patna","delhi","mumbai","kolkata","bangalore"))
# function1(list1)


# return values : 

# def returvalue(num):
#     return 7 * num

# print(returvalue(7))

# the pass statements : 

# function definition can not be empty, but if we for some reason have a function definition with no content, put pass statement to avoid getting an error.

# def emptyfunction():
#     pass

# positional only arguments : 

# we can specify that a function can have only positional arguments, or only keyword arguments.

# to specify that a function can have only positional arguments, add , / after the arguments:

# def function1(x,/):
#     print(x)
# function1(3)

# without the , / we arctually allowed to use keyword arguments even if the function expects positional arguments : 

# def function1(x):
#     print(x)
# function1(x=3)


# keyword only arguments : 

# to specify that a function can have only keyword arguments, add *,before the arguments : 

# def function1(*,x):
#     print(x)

# function1(x = 4)

# without the *, we are allowed to use positional arguments even if the function expects keywords arguments : 

# def function1(x):
#     print(x)

# function1(4)


# combine positional only and keyword only : 

# any arguments before the / , are positional-only, and any arguments after the *, are keyword-only.

# def function1(a,b,/,*,c,d):
#     print(a+b+c+d)

# function1(5,6,c=7,d=8)


# Recursion : 

# python also accept function recursion, which means a defined function can call itself : 

def function1(num):
    if num == 0:
        return 0
    return num + function1(num - 1)

print(function1(5))