# Creating a 5x5 grid initialized with zeros
rows, cols = 5, 5
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))
    print()

# Example usage
print("Initial Grid:")
print_grid(grid)

# Updating some values in the grid
grid[2][3] = 1
grid[4][4] = 2

print("Updated Grid:")
print_grid(grid)
