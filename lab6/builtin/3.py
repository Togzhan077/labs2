#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
s = s.replace(' ', '') 
if s == s[::-1]:
    print("Oh yea")
else:
    print("nope")