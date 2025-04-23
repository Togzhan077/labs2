#Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple=( "banana", "cherry", "apple")
print(thistuple)

#tuples are sllow duplicates
t = ("banana", "cherry", "banana", "cherry")
print(t)

#To determine how many items a tuple has, use the len() function:
print(len(t))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple=("apple",)
print(type(thistuple))

#not a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items can be of any data type:
tuple1=(1,2,3,4,5)
tuple2=("banana", "apple", "cherry")
tuple3= (True, False, False)

#A tuple can contain different data types:
tuple=("banana", True, 1)

#type() = <class, 'typle'>
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple))

# tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)