#Write a Python program with builtin function that accepts a string and calculate 
#the number of upper case letters and lower case letters
s = input()
upper_count = 0
lower_count = 0
for char in s:
    if char.isupper():
        upper_count += 1
for char in s:
    if char.islower():
        lower_count += 1

print(upper_count)
print(lower_count)
    