#access set items

#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

set1 = {"apple", "banana" , "cherry"}
for x in set1:
    print(x)

print("-")
#Check if "banana" is present in the set
print( "banana" in set1)
print("-")

#Check if "banana" is NOT present in the set:
print("banana"  not in set1)