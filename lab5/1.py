#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = "aaaabbbbbbbbbb"
x = re.search('a*b*', text)
print(x)