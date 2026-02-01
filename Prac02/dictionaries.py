#1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#output: Ford

#3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict)) #output: 3
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#4
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model") #output: Mustang
x = thisdict.keys() #output: dict_keys(['brand', 'model', 'year'])
x = thisdict.values() #output: dict_values(['Ford', 'Mustang', 1964])
x = thisdict.items() #output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print(x) 

#5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) 
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#6
#Pop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#output: {'brand': 'Ford', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#same as pop

#7
#Popitem
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#output: {'brand': 'Ford', 'model': 'Mustang'}

#8
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 
#output: {}

#9
#Values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Keys
for x in thisdict.keys():
  print(x)

#Both
for x, y in thisdict.items():
  print(x, y)