"Simulate a grid of nested lists; coordinates of pixels."""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#print(len(grid[0]))

# Initialises variable to be used to as an index to access the internal lists of grid
in_arr = 0

# Outside for-loop allows access to the lengths of nested lists.
# Also helps to index into the list in grid.
for i in range(len(grid[in_arr])):
    # Loops the length of list value grid.
    for j in range(len(grid)):
        # j index to elements of grid
        # i allows us to index in each element of the list nested in grid.
        print(grid[j][i], end=' ')      # Outputs the elements of the nested list elements of list value grid
    print()
    in_arr += 1 
