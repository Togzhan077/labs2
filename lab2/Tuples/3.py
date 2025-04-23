#update tuples

#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there are some workarounds.

#Convert the tuple into a list to be able to change it:
x=("apple", "banana", "cherry")
y=list(x)
y[1]= "kiwi"
x=tuple(y)
print(x)

#add items
thistuple = ("banana", "apple", "cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

#Add tuple to a tuple - you are allowed add tuple to tuple:
tuple1 = ("apple" , "banana" , "cherry")
y=("orange",)
tuple1+=y
print(tuple1)

#Remove items - You cannot remove items in a tuple.
#but you can use the same workaround as we used for changing and adding tuple items:
tuple2 = ("apple" , "banana", "cherry")
y=list(tuple2)
y.remove("apple")
tuple2=tuple(y)
print(tuple2)

#you allow delete  the tuple completely
tuple3 = ("banana", "cherry" , "apple")
del tuple3
print(tuple3)
#this will raise an error because the tuple no longer exists