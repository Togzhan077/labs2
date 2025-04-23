def even_numbers(n):
    for i in range(0, n+1, 2):  # Step 2 ensures that we get only even numbers
        yield i

# Input from user
n = int(input("Enter the value of n: "))

# Generate even numbers
even_nums = even_numbers(n)
print(", ".join(map(str, even_nums)))
