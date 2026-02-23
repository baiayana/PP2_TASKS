#1
n = int(input())
sq = (x*x for x in range(1, n + 1))
for i in sq:
    print(i)

#2
n = int(input())
even = (x for x in range(0, n + 1) if x % 2 == 0)
print(", ".join(map(str, even)))

#3
def divisible(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for v in divisible(n):
    print(v)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i*i

a = int(input())
b = int(input())

for v in squares(a, b):
    print(v)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for v in countdown(n):
    print(v)