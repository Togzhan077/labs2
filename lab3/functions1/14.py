# game_and_utilities.py

import random
import math

# Task 1: Function to check if a string is palindrome
def is_palindrome(s):
    cleaned_str = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_str == cleaned_str[::-1]

# Task 2: Function to print a histogram for a list of integers
def histogram(nums):
    for num in nums:
        print('*' * num)

# Task 3: Function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Task 4: Function to check if the list contains 0, 0, 7 in order
def spy_game(nums):
    sequence = [0, 0, 7]
    for num in nums:
        if num == sequence[0]:
            sequence.pop(0)
        if not sequence:
            return True
    return False

# Task 5: Function to return unique elements from a list
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Task 6: Function to generate all permutations of a string
import itertools
def print_permutations(s):
    permutations = itertools.permutations(s)
    for perm in permutations:
        print(''.join(perm))

# Task 7: Function for the "Guess the Number" game
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
