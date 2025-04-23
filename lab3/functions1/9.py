# Function to return a list with unique elements
def unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    # Iterate through the input list
    for item in input_list:
        # If the item is not already in the unique list, add it
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Example usage:
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
result = unique_elements(input_list)
print(f"List with unique elements: {result}")
