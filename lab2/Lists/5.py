#Remove List Items
list = ["apple", "banana", "cherry", "banana", "kiwi"]
list1 = ["tomato" , "potato" , "cucumber" , "carrot"]

#The remove() method removes the specified item.
list.remove("apple")
print(list)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
list.remove("banana")
print(list)

#The pop() method removes the specified index.
list.pop(0)
print(list)

#If you do not specify the index, the pop() method removes the last item.
list.pop()
print(list)

#The del keyword also removes the specified index:
del list1[2]
print(list1)

#The del keyword can also delete the list completely.
del list
print(list)

#The clear() method empties the list.
#The list still remains, but it has no content.
list1.clear()
print(list1)