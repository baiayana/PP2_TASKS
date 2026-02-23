#1
import math 

deg = float(input("Input degree: "))
rad = deg * math.pi / 180

print(f"Output radian: {rad:.6f}")

#2
import math
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
area_trapezoid = (b1+b2)/2 * h
print(f"Expected Output: {area_trapezoid}")

#3
import math
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s * s) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area:.0f}")

#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print(f"Expected Output: {area}")
