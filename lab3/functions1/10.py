# Function to check if a given word or phrase is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_str = ''.join(e for e in s if e.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
input_str = input("Enter a word or phrase: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome!")
else:
    print(f"'{input_str}' is not a palindrome.")
