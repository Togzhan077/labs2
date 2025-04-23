# Define the function to convert Fahrenheit to Centigrade
def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Read the Fahrenheit temperature from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Call the function and store the result
centigrade = fahrenheit_to_centigrade(fahrenheit)

# Display the result
print(f"The equivalent temperature in Centigrade is: {centigrade:.2f}°C")
