#1
#create class
class MyClass:
  x = 5

#2
#create object
p1 = MyClass()
print(p1.x)

#3
#delete objects
del p1

#4
#multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#5
#if class is emty use pass
class Person:
  pass