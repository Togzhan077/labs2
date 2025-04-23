#Almost any value is evaluated to True if it has some sort of content.

#Any strings is true except empty strings
print(bool("abs"))
print(bool(""))

#Any number is True, except 0.
print(bool(45))
print(bool(0))

#Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(["apple" , "cherry" , "banana"]))
print(bool([]))
