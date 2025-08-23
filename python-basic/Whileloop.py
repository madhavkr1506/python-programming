# python has two primitive loop commands : 

# while loop
# for loop

# with the while loop we can execute a set of statements as long as a condition is true.

# i=1
# while i <= 10:
#     print(i," x ",10," = ", i * 10)
#     i += 1

# remember to increment i, or else the loop will continue forever.
    
# break statement : 

# it will stop the loop even if the while condition is true : 

# i=1
# while i <= 10:
#     print(i," x ",10," = ", i * 10)
#     if(i == 5):
#         break
#     i += 1
    
# the continue statement : 

# will stop the current iteration, and continue with next : 
    
# i=0
# while i < 10:
#     i += 1
#     if(i == 5):
#         continue
#     print(i," x ",10," = ", i * 10)


# the else statement : 

# with the else statement we can run a block of code once when the condition no longer is true : 

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
    
    