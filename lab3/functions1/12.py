import random

def guess_the_number():
    # Greet the user
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    # Randomly choose a number between 1 and 20
    secret_number = random.randint(1, 20)
    
    # Initialize the guess count
    guesses_taken = 0
    
    while True:
        # Prompt the user to make a guess
        print("Take a guess.")
        guess = int(input())  # Convert input to an integer
        
        # Increment the number of guesses
        guesses_taken += 1
        
        # Check if the guess is too low, too high, or correct
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break  # Exit the loop when the guess is correct

# Run the game
guess_the_number()
