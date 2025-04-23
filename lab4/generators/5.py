def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Input from user
n = int(input("Enter the value of n: "))

# Generate countdown
countdown_gen = countdown(n)
for num in countdown_gen:
    print(num)
