#Loop Lists
list = ["apple", "banana", "cherry"]

#You can loop through the list items by using a for loop:
for x in list:
    print(x)
    
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
for i in range(len(list)):
    print(list[i])
    
#Using a While Loop
i = 0
while i < len(list):
  print(list[i])
  i = i + 1

#Looping Using List Comprehension
[print(x) for x in list]