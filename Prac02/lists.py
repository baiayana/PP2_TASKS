'''
LIST is a collection which is ordered and changeable. Allows duplicate members.
TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
SET is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
DICTIONARY is a collection which is ordered** and changeable. No duplicate members.
'''
#1
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #output: 3
#2
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#3
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#5
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#7
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #output: ['apple', 'watermelon']


#8
#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #output: ['apple', 'orange', 'banana', 'cherry']
#extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)


#9
#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  #output: ['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  #output: ['apple', 'cherry', 'banana', 'kiwi']

#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  #output: ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  #output: ['apple', 'banana']

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  #output: ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  #output: []


#10
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)   
'''output: apple 
           banana 
           cherry'''

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #output: ['apple', 'banana', 'mango']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #same as above

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)


newlist = [x for x in range(10)]
print(newlist) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


newlist = [x for x in range(10) if x < 5] #output: [0, 1, 2, 3, 4]


newlist = [x.upper() for x in fruits] #output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#11
#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]

#descending sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #['Kiwi', 'Orange', 'banana', 'cherry']

#reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']

