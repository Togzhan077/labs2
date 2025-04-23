from datetime import datetime

# Қазіргі күн мен уақытты алу
current_time = datetime.now()

# Микросекундтарды алып тастау
current_time_without_microseconds = current_time.replace(microsecond=0)

# Нәтижені шығару
print("Қазіргі уақыт:", current_time)
print("Микросекундсыз уақыт:", current_time_without_microseconds)
