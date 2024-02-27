# a lambda function is a small anonymous function.
# a lambda function can take any number of arguments, but can only have one expression.

# syntax : lambda arguments : expression

# the expression is executed and the result is returned:


# x = lambda a : a + 10
# print(x(5))

# name = lambda fname : fname +" "+ "Kumar"
# print(name("Madhav"))


# multiply = lambda a,b,c : a*b*c
# print(multiply(a = 5,b = 4,c = 6))



# why use lambda functions : 

# the power  of lambda function is better shown when you use them as an anonymous function inside another function : 

def function1(num):
    return lambda a : a * num

temp = function1(11)
print(temp(15))