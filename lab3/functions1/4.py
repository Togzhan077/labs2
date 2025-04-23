import math

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Main function to filter prime numbers from the list
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = filter_prime(numbers)
print(f"Prime numbers: {prime_numbers}")
