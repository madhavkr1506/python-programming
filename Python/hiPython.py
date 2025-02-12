# class parent :
#     @staticmethod
#     def printHello() :
#         print("hello from parent class")


# class child(parent) : 
#     # pass
#     @staticmethod
#     def printHello() :
#         print("hello from child class")


# class subchild(child) :
#     # pass
#     def printHello(self) :
#         print("hello from sub child class")

# object = subchild()
# object.printHello()





# class parent : 
#     def takeInput(self) : 
#         print("Enter your name: ")
#         name = str(input())
#         return name


# class child(parent) : 
#     def __init__ (self, name) :
#         self.name = name

#     def printName(self) :
#         print("My name is " + self.name)
    

# parentObject = parent()
# name = parentObject.takeInput()
# childObject = child(name)
# childObject.printName()



# class parent : 
#     def printHello(self) : print("hello from parent class")

# class child(parent) : 
#     def printHello(self) : 
#         super().printHello()
#         print("hello from child class")

# childObject = child()
# childObject.printHello()

