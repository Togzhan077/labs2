#if statement

print("if:")
a=200
b=33
if a>b:
    print("a greater than b")

#elif - if the previous conditions were not true, then try this condition
print("elif:")
a=33
b=33
if a>b:
    print("a greater than b")
elif a==b:
    print("a equal to b")

#else - The else keyword catches anything which isn't caught by the preceding conditions.
print("else:")
a=33
b=100
if a>b:
    print("a greater than b")
elif a==b:
    print("a equal to b")
else:
    print("b greater than a")
