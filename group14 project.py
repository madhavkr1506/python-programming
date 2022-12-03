print("-"*125)
print("\t\t\t\t\t\twelcome to student repository")# heading of project
print("-"*125)
dict1={"madhav":"1234567890","nishkarsh":"0987654321","satvik":"9876543012"}

#getting details by student name

def dsearch(skey,dict1):
 if len(skey)==0:
  print("student not found in repository")
 elif len(skey)>0:
  print("contact number of {} is".format(skey),dict1.get(skey))

#getting respository update

def dupdate(dict1):
 dk=input('Enter the student name for which you want to update contact number: ')
 if dk not in dict1.keys():
  print('!!!!Student not present in respository!!!!')
 elif dk in dict1.keys():
  dv=input("Enter new 10 digit contact number:")
  if len(dv) > 10 or len(dv) < 10:
   print('!!!!Length of contact number should be 10 digit!!!!')
  elif dk in dict1.keys() and len(dv) == 10:
   print(dict1.update({dk:dv}))
   print('Updated respository->', dict1)

# adding new details in respository

def dadd(dict1):
 nkey=input("Enter student name which you want to add in repository:")
 nvalue=input("Enter his 10 digit phone number:")
 if len(nvalue)==10:
  dict1[nkey]=nvalue
  print("Updated repository->",dict1)
 else:
  print("Enter correct credentials")

# getting multiple students detalis displayed

def getmultiple(n,dict1):
 l1=[]
 for i in range(n):
  a=input("Enter student name:")
  l1.append(a)
 for j in l1:
  print(j,"-",dict1[j])


# displaying whole dictionary


def display(dict1):
 print(dict1)
while True:
 print("-"*40)
 print("\t Choose An Operation ")
 print("-"*40)
 print("Press 1 - Get contact no. of student by name")
 print("Press 2 - Update respository")
 print("Press 3 - Add student in respository")
 print('Press 4 - Display multiple student contact no.')
 print("Press 5 - Display whole respository")
 print('Press 6 - Quit')
 ch = int(input("Enter Your Choice : "))
 if ch==1:
  skey=input("Enter student name:")
  dsearch(skey,dict1)
 elif ch==2:
  dupdate(dict1)
 elif ch==3:
  dadd(dict1)
 elif ch==4:
  n=int(input("Enter number of student for which you want contact number: "))
  getmultiple(n,dict1)
 elif ch==5:
  display(dict1)
 elif ch==6:
  break
 else:
  print("!!Please choose correct option!!")











