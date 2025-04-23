def divisible_by_3_and_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Input from user
n = int(input("Enter the value of n: "))

# Generate numbers divisible by 3 and 4
divisible_numbers = divisible_by_3_and_4(n)
print(", ".join(map(str, divisible_numbers)))
