import math  # Add this line to import the math module

# Input values
n_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the length of one side: "))

# Calculate the area of the regular polygon
area = (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))

# Output result
print(f"The area of the polygon is: {area:.1f}")
