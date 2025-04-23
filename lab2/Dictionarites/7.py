#Copy dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
print(mydict)
print("-")

#Make a copy of a dictionary with the dict() function:
mydict=dict(thisdict)
print(thisdict)