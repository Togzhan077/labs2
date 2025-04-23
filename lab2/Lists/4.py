#Add list items
thelist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

#Append items - to add an item to the end of the list, use the append() method:
thelist.append("orange")
print(thelist)

#Insert Items - арнайы бір индекс орнына қоямыз, не заменяем
thelist.insert(1 , "orange")
print(thelist)

#Extend list - To append elements from another list to the current list, use the extend() method
thelist.extend(tropical)
print(thelist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thistupple = ( "kiwi" , "orange")
thelist.extend(thistupple)
print(thelist)