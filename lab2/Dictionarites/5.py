#Remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color" : "black"
}

#The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)
print("-")

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
del thisdict["brand"]
print(thisdict)

#The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

#The del keyword can also delete the dictionary completely:
del thisdict
print(thisdict) #print error becase this dict no longer exists