# Function to reverse the words in a given sentence
def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Accept input from the user
user_input = input("Enter a sentence: ")

# Call the function and print the reversed sentence
print(reverse_words(user_input))
