#A set is a collection which is unordered, unchangeable*, and unindexed. {}
#Set items are unchangeable, but you can remove items and add new items.

myset = {"apple" , "banana" , "cherry"}
print(myset)
print("-")

#Sets cannot have two items with the same value.
set1 = {"apple" , "banana" , "apple"}
print(set1)
print("-")

#he values True and 1 are considered the same value in sets, and are treated as duplicates:
set2 = {1, 2 , 3 , True}
print(set2)
print("-")

#False and 0 is considered the same value:
set3 = {0 , 1 ,2, 3, False}
print(set3)
print("-")

#To determine how many items a set has, use the len() function.
print(len(set3))
print("-")

#Set items can be of any data type:
set4 = {"a" , "b" , "c"}
set5 = {1,2,3}
set6= {True , False}
set7 = { "a", 2 , True}
print(set4)
print(set5)
print(set6)
print(set7)
print("-")

#type = <class 'set'>
print(type(set7))

#the set constructor()
set8 = set(("apple", "banana" , "cherry"))
print(set8)