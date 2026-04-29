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

in_arr = 0
for i in range(len(grid[in_arr])):
    for j in range(len(grid)):
        print(grid[j][i], end=' ')
    print()
    in_arr += 1
