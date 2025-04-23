from datetime import datetime, timedelta

# Қазіргі күнді алу
today = datetime.now()

# Кешегі күнді табу
yesterday = today - timedelta(days=1)

# Ертеңгі күнді табу
tomorrow = today + timedelta(days=1)

# Нәтижелерді шығару
print("Бүгінгі күн:", today.strftime("%Y-%m-%d"))
print("Кешегі күн:", yesterday.strftime("%Y-%m-%d"))
print("Ертеңгі күн:", tomorrow.strftime("%Y-%m-%d"))
