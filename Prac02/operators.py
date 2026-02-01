#1
#Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y) #returns a float: 3,75
print(x % y)
print(x ** y)
print(x // y) #returns an integer: 3


#2
#Assignment Operators
'''	
x += 3	x = x + 3	
x -= 3	x = x - 3	
x *= 3	x = x * 3	
x /= 3	x = x / 3	
x %= 3	x = x % 3	
x //= 3	x = x // 3	
x **= 3	x = x ** 3	
x &= 3	x = x & 3	
x |= 3	x = x | 3	
x ^= 3	x = x ^ 3	
x >>= 3	x = x >> 3	
x <<= 3	x = x << 3	
print(x := 3)	x = 3 print(x)'''

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


#3
#Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5

print(1 < x < 10) #True

print(1 < x and x < 10) #True


#4
#Logical Operators
x = 5


print(x > 0 and x < 10) #True
print(x < 5 or x > 10) #False
print(not(x > 3 and x < 10)) #False


#5
#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True
print(x is y) #False
print(x == y) #True
print(x is not y) #True


#6
#Membership Operators
text = "Hello World"

print("H" in text) #True
print("hello" in text) #False
print("z" not in text) #True


#7
#Btwise Operators
print(6 & 3) #AND
print(6 | 3) #OR
print(6 ^ 3) #XOR