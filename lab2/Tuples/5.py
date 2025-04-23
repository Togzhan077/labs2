#Loop tuples
tuple1 = ("banana", "apple" , "orange" , "cherry" , "strawberry")

#You can loop through the tuple items by using a for loop.
for x in tuple1:
    print(x)

print("-")
    
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
for i in range(len(tuple1)):
    print(tuple1[i])
    
print("-")
    
#While loop
i=0
while i<len(tuple1):
    print(tuple1[i])
    i+=1

