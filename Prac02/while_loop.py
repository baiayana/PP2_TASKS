#1
x = 0

while x < 9:
  print(x)
  x = x + 1

#2
i = 1
while i < 6:
  print(i)
  i += 1

#3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#4
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#5
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")