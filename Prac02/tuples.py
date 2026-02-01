#1
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#2
tuple1 = ("abc", 34, True, 40, "male")
#3
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #output: banana
#4
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)#tuples sre unchangeable, but in this case we can 
#5
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)#output: ('apple', 'banana', 'cherry', 'orange')
#6
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#7
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


#8
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
'''output: apple
           banana
           ['cherry', 'strawberry', 'raspberry']
'''

#9
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) #output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

'''count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found'''