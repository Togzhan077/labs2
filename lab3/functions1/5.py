import itertools

# Function to print all permutations of a given string
def print_permutations(s):
    # Use itertools.permutations to generate all permutations
    permutations = itertools.permutations(s)
    
    # Convert permutations to strings and print them
    for perm in permutations:
        print(''.join(perm))

# Accept string input from the user
user_input = input("Enter a string: ")

# Call the function to print all permutations
print_permutations(user_input)
