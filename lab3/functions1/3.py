def solve(numheads, numlegs):
    # Let x be the number of chickens and y be the number of rabbits
    # Equation 1: x + y = numheads
    # Equation 2: 2x + 4y = numlegs
    
    # Solve the system of equations:
    # From Equation 1, we know x = numheads - y
    # Substitute x into Equation 2:
    # 2(numheads - y) + 4y = numlegs
    # 2*numheads - 2y + 4y = numlegs
    # 2*numheads + 2y = numlegs
    # 2y = numlegs - 2*numheads
    # y = (numlegs - 2*numheads) / 2
    
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    
    return x, y

# Example usage
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
