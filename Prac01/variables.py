#Pyhton variables
#1
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#2
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#3
x = 5
y = "John"
print(type(x))
print(type(y))
#4
x = "John"
# is the same as
x = 'John'
#5
a = 4
A = "Sally"
#A will not overwrite a

#Variable Names
#legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#illegal
'''2myvar = "John"
my-var = "John"
my var = "John"'''

#Assign Multiple Values
#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#2
x = y = z = "Orange"
print(x)
print(y)
print(z)
#3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables 
#1
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#2
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#3
x = 5
y = 10
print(x + y)
#4
x = 5
y = "John"
print(x + y)#Not right you can not combine str with int
#5
x = 5
y = "John"
print(x, y)

#Global variables
#variables that are created outside of the function are known as global
#global variable can both used inside and outside
#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 
#2
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
#The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#3
#To create a global variable inside a function, you can use the global keyword.
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)