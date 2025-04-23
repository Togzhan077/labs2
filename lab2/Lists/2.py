#Access List Items
list = ["apple" , "banana", "cherry" , "orange" , "kiwi" , "lemon" ]
print(list[1])
#The first item has index 0.

#Negative indexing - means start from the end
print(list[-1])

#Range of Indexes -you can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items

print(list[2:5]) #The search will start at index 2 (included) and end at index 5 (not included)

#By leaving out the start value, the range will start at the first item:
print(list[:4])

#By leaving out the end value, the range will go on to the end of the list:
print(list[2:])

#Range of Negative Indexes - логический дәл бағанағыны артынан бастайды
print(list[-4:-1])

#Check if Item Exists - To determine if a specified item is present in a list use the in keyword:
if "apple" in list:
    print("Yes")
else:
    print("No")

