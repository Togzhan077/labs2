def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2

# Пайдалану мысалы
N = 10  # Мысал үшін N мәні 10 деп аламыз
squares_generator = generate_squares(N)

# Генераторды шығару
for square in squares_generator:
    print(square)
