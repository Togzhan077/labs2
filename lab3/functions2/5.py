movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# movies_functions.py

# Функция для проверки, что фильм имеет IMDB выше 5.5
def is_good_movie(movie):
    return movie['imdb'] > 5.5

# Функция для фильтрации фильмов с IMDB выше 5.5
def filter_good_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# Функция для фильтрации фильмов по категории
def filter_by_category(movies, category):
    return [movie for movie in movies if movie['category'].lower() == category.lower()]

# Функция для вычисления среднего IMDB балла
def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

# Функция для вычисления среднего IMDB балла по категории
def average_imdb_score_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    if not category_movies:
        return 0
    return average_imdb_score(category_movies)

# Example 5: Calculate the average IMDB score for movies in the "Romance" category
avg_imdb_romance = average_imdb_score_by_category(movies, "Romance")
print("Average IMDB score for Romance movies:", avg_imdb_romance)
