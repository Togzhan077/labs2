# Function to check if the list contains 0, 0, 7 in order
def spy_game(nums):
    # Initialize a variable to track the sequence of [0, 0, 7]
    sequence = [0, 0, 7]
    
    # Iterate through the list and check if the sequence appears in order
    for num in nums:
        if num == sequence[0]:  # If the current number matches the first element of the sequence
            sequence.pop(0)  # Remove the matched number from the sequence
        if not sequence:  # If the sequence is empty, it means we've found 0, 0, 7
            return True
    
    return False  # If the loop finishes without finding the sequence, return False

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Should return True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Should return True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Should return False
