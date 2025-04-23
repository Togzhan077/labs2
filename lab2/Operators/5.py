#Identity operators

#Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

x=5
y=3

#is - Returns True if both variables are the same object

print(x is y)

# is not - Returns True if both variables are not the same object

print( x is not y)