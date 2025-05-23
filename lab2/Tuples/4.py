#Unpack tuples

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
tuple1=("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow , red) = tuple1
print(green)
print(yellow)
print(red)

print("-")

#The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.

#Assign the rest of the values as a list called "red":
tuple2= ("apple", "banana", "cherry", "strawberry", "raspberry")
(green , yellow, *red) = tuple2
print(green)
print(yellow)
print(red)

print("-")

#If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.
(green , *yellow , red) = tuple2
print(green)
print(yellow)
print(red)