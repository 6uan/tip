'''
Problem 7: Diagonal
Write a function diagonal_sum() that accepts a 2D n x n matrix grid and returns the sum of the matrix diagonals. Only include the sum of all the elements on the primary diagonal and all the elements in the secondary diagonal that are not part of the primary diagonal.

The primary diagonal is all cells in the matrix along a line drawn from the top-left cell in the matrix to the bottom-right cell. The secondary diagonal is all cells in the matrix along a line drawn from the top-right cell in the matrix to the bottom-left cell.

def diagonal_sum(grid):
	pass
Example 1 input matrix with primary and secondary diagonals labelled

Example Usage

grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum(grid)

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
diagonal_sum(grid)

grid = [
	[5]
]
diagonal_sum(grid)
Example Output:

25
8
5
'''

def diagonal_sum(grid):
    n = len(grid)
    sum = 0
	
    for i in range(n):
        sum += grid[i][i]
        sum += grid[i][n - 1 - i]

    if n % 2 != 0:
        sum -= grid[n//2][n//2]

    return sum


grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(grid))

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid))


grid = [
	[5]
]
print(diagonal_sum(grid))
