#Remove set items

print("remove()")
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

print("discard()")
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

print("pop()")
#You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

print("clear()")
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

print("delete()")
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)