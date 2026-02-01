#1
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'banana', 'cherry', 'apple'}
#duplicates are not allowed

#2
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#output: {True, 2, 'banana', 'cherry', 'apple'}
#True and 1 is considered the same value

#3
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#output: {False, True, 'cherry', 'apple', 'banana'}

#4
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#output: {True, 34, 40, 'male', 'abc'}

#5
#ADD METHOD
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#output: {'apple', 'banana', 'cherry', 'orange'}

#6
#UPDATE METHOD
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#output: {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#7
#method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#8
#REMOVE METHOD
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#{'cherry', 'apple'}
#Note: If the item to remove does not exist, remove() will raise an error.

#9
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#{'cherry', 'apple'}
#Note: If the item to remove does not exist, discard() will NOT raise an error.

'''You can also use the pop() method to remove an item, but this method will remove 
a random item, so you cannot be sure what item that gets removed.'''

#The clear() method empties the set

#The del keyword will delete the set completely



#LOOP
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
'''output: cherry
           banana
           apple'''