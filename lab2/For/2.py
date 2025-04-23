#Break statement
fruits = ["apple", "banana" , "cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

print("-")

#Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits:
    if x=="banana":
        break
    print(x)

print("-")

#Continue statement
for x in fruits:
    if x=="banana":
        continue
    print(x)
    
print("-")
    
#Else statement
for x in range(6):
    print(x)
else:
    print("Finally finished")