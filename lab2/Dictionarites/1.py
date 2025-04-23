#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dict1 = {
    "Brand" : "Ford",
     "Model" : "Mustang",
     "year" : 1964
}
print(dict1)
print("-")

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(dict1["Brand"])
print("-")

#Duplicates Not Allowed
dict2 = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2020,
    "year" : 1964
}
print(dict2)
print("-")

#to determine how many items a dictionary has, use the len() function:
print(len(dict2))

#he values in dictionary items can be of any data type:
dict3 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(dict3)
print("-")

#type() - <class 'dict'>
print(type(dict3))
print("-")

#the dict() constructor
dict4=dict(name="Togzhan", year=18, country="Kazakhstan")
print(dict4)