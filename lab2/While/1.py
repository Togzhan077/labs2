#With the while loop we can execute a set of statements as long as a condition is true.
i=1
while i<6:
    print(i)
    i+=1
    
print("-")
    
#break
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
print("-")

#continue
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

print("-")
    
#else - With the else statement we can run a block of code once when the condition no longer is true:
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
