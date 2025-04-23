from datetime import datetime

# Екі күнді енгізу (қажетті форматты пайдаланамыз: YYYY-MM-DD HH:MM:SS)
date1 = datetime(2025, 2, 21, 12, 30, 0)  # бірінші күн
date2 = datetime(2025, 2, 22, 14, 45, 0)  # екінші күн

# Екі күннің айырмасын есептеу
difference = date2 - date1

# Айырманы секундқа түрлендіру
seconds_difference = difference.total_seconds()

# Нәтижені шығару
print("Екі күннің айырмасы секундпен:", seconds_difference)
