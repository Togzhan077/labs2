#Nested dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.

#Create a dictionary that contain three dictionaries:
myfamily = {
    "child1" : {
        "name" : "Togzhan",
        "year" : 18
    },
    "child2" : {
        "name" : "Shugyla",
        "year" : 18
    },
    "child3" : {
        "name" : "Sultan",
        "year" : 10
    }
    
}

print(myfamily)
print("-")

#if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)