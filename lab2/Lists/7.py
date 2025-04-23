#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#this code with comprehision
newlist = [x for x in fruits if "a" in x]

print(newlist)

#without if condition
newlist = [x for x in fruits]

print(newlist)

#Iterable - You can use the range() function to create an iterable:
list = [x for x in range(10)]
print(list)

#same example, but with a condition
list1 = [x for x in range(10) if x<5]
print(list1)

#Expression 
#1 Set the values in the new list to upper case:
newlist = [ x.upper() for x in fruits]
print(newlist)

#2 Set all values in the new list to 'hello':
newlist = [ "hello" for x in fruits ]
print(newlist)

#3 Return "orange" instead of "banana":
newlist = ["banana" for x in fruits if x=="hello"]
print(newlist)
