import math

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    # Using the formula V = (4/3) * π * r^3
    volume = (4/3) * math.pi * radius**3
    return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
print(f"The volume of the sphere is: {sphere_volume(radius):.2f}")
