#Add set items

#Once a set is created, you cannot change its items, but you can add new items.

#add() method
set1 = { "banana", "apple", "orange"}
set1.add("cherry")
print(set1)
print("-")

#To add items from another set into the current set, use the update() method.
set2 = {"carrot", "potato", "tomato"}
set1.update(set2)
print(set1)
print("-")

#he object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
set3 = (1,2,3)
set1.update(set3)
print(set1)
print("-")