#Python Strings
#slicing
#1
b = "Hello, World!"
print(b[2:5])
#2
b = "Hello, World!"
print(b[:5])
#3
b = "Hello, World!"
print(b[2:])
#4
b = "Hello, World!"
print(b[-5:-2])

#Modify Strings
#1
a = "Hello, World!"
print(a.upper())
#2
a = "Hello, World!"
print(a.lower())
#3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#4
a = "Hello, World!"
print(a.replace("H", "J"))
#5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenate Strings
#1
a = "Hello"
b = "World"
c = a + b
print(c)
#2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format Strings 
#1
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#2
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #result: The price is 59.00 dollars
#3
txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north." #result: We are the so-called "Vikings" from the north.