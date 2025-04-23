#Access items

#You can access the items of a dictionary by referring to its key name, inside square brackets:
dict1 = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : "1964"
    }
x=dict1["model"]
print(x)
print("-")

#There is also a method called get() that will give you the same result:
x=dict1.get("year")
print(x)
print("-")

#The keys() method will return a list of all the keys in the dictionary.
x=dict1.keys()
print(x)
print("-")

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
dict1["color"]="white"
print(x)
print("-")

#The values() method will return a list of all the values in the dictionary.
x=dict1.values()
print(x)
print("-")

#The list of the values is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the values list.
dict1["year"]=2020
print(x)
print("-")

#The items() method will return each item in a dictionary, as tuples in a list.
x=dict1.items()
print(x)
print("-")

#The returned list is a view of the items of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the items list.
dict1["color"] = "black"
print(x)
print("-")

#To determine if a specified key is present in a dictionary use the in keyword:
if "model" in dict1:
    print("Yes")
