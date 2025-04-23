#Write a Python program that invoke square root function after specific milliseconds
#Sample Input:
"""
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""
import time

number = int(input())
milliseconds = int(input())
time.sleep(milliseconds/1000)
square = number ** 0.5
print('Square root of', number, 'after', milliseconds, 'is', square)