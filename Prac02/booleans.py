#1
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
#2
print(bool("Hello")) #True
print(bool(15)) #True
#3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#4
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#5
#cases when ouput is false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#6
#function, which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))