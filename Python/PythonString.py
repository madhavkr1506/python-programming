# multiline strings in python : 
# we can assign multiline string to a variable by using three quotes.

# string1 = """madhav is 
# a good boy,
# he is learning data science."""
# print(string1)


# string2 = '''madhav is 
# a good boy,
# he is learning data science.'''
# print(string2)

# string as array
# print(string2[0])

# python does not have a character data type , a single character is simply a string of length of 1.
# square brackets can be used to access elements of the string.

# looping through a string

# string3 = "Madhav"

# for x in string3:
#     print(x)


# string len() function:
    
# print(len(string3))

# check string : 

# string4 = "Madhav is a good boy"
# print("a" in string4)

# use it in an if statements : 

# if("a" in string4):
#     print("yes, it is in string4")
# else:
#     print("no, it is not in string4")

# check if not

# print("a2" not in string4)

# use it in an if statement

# if("a2" not in string4):
#     print("it is not in string4")
# else:
#     print("it is in string4")


# slicing string

# text = "Madhav is a good boy"
# print(text[0:6]) #get the character from position 0 to position 6 (not included)

# first character has index 0

# get the character from the start to position 5(not included)
# print(text[:5])

# slicing to the end

# print(text[2:]) # by leaving out the end index , the range will go to the end

# negative indexing 

# name = "Madhav"
# print(name[-6:-2])

# modify string :

# the upper() method returns the string in upper case:

# name = "Madhav"
# print(name.upper())


# the lower() method returns the string in lower case:

# print(name.lower())

# remove whitespaces : 
# whitespace is the space before and / or after actual text, and very often you want to remove this space.
# surname="        kumar "
# print(surname.strip())

# replace string

# string = "Madham"
# print(string.replace("m","v"))

# split string

# string = "Madhav kumar"

# print(string.split(" "))


# string concatenation 

# name = "Madhav"
# surname = "Kumar"
# fullname = name +" "+ surname
# print(fullname)

# formate string

# age = 20
# txt = "My age is " + age # it will throw an error
# txt = "My age is {}"
# print(txt.format(age))

# we can combine string and number by using the format() method.
# the format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are : 

# quantity = 3
# itemno = 256
# price = 100.2
# myoredr1 = "I want {} pieces of item {} for {} dollars."
# print(myoredr1.format(quantity,itemno,price))

# myoredr2 = "I want to pay {2} for {0} pieces of item {1}."
# print(myoredr2.format(quantity,itemno,price))


# escape character : 
# to insert characters that are illegal in a string, use an escape character.

# an escape character is a backlash \ followed by the character you want to insert.

# an example of an illegal character is a double quote inside a string that is surrounded by double quotes : 

# txt = "My name is \"Madhav\" from the North."  #to fix this problem we use escape character \" :
# print(txt)

# other escape character in the python : 
# \' single quote
# \\ backslash
# \n new line
# \r carriage return
# \t tab
# \b backspace
# \f from feed
# \ooo octal value
# \xhh hex value

# some set of string built in methods in python : 

# capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(), find(), format(),
# format_map(), index(), isalnum(), isalpha(), isascii(), isdecimal(),
# isdigit(), islower(), isnumeric(), isspace(), istitle(), isupper(),
# join(), lower(), lstrip(), rstrip(), rfind(), rindex(), partition(),strip(), split(),
# swapcase(), title(), upper(),zfill(), startswith() etc.
