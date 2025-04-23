from datetime import datetime, timedelta

# Get the current date and time
current_date = datetime.now()

# Subtract 5 days from the current date
new_date = current_date - timedelta(days=5)

# Print the result
print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))
