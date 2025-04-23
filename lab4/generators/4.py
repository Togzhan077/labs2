def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

# Input from user
a = int(input("Enter the starting number a: "))
b = int(input("Enter the ending number b: "))

# Generate squares of numbers from a to b
squares_gen = squares(a, b)
for square in squares_gen:
    print(square)
