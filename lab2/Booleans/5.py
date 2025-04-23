#You can create functions that returns a Boolean Value:

#True
def myfunction():
    return True
print(myfunction())

#Print "YES!" if the function returns True, otherwise print "NO!":

#myversion
def myfun2():
    return True
if bool(myfunction())==True:
    print("Yes")
else:
    print("No")
    
#versionW
def myfun3():
    return False
if myfun3():
    print("Yes")
else:
    print("No")