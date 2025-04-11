'''
Problem 1: Seeking Safety
The city has been overrun by zombies, and you need to be very careful about how you move about the city. You have a map of the city grid represented by an m x n matrix of 1s (safe zones) and 0s (infected zones). Given a tuple position in the form (row, column) representing your current position in the city grid, implement a function next_moves() that returns a list of tuples representing safe next moves. You may return the moves in any order.

From your current position, you may move to any (row, column) index that is horizontally or vertically adjacent such that row and column are both valid indices in grid. A move is safe if it has value 1.

def next_moves(position, grid):
    pass
Example Usage:

grid = [
    (0)(1)(2)(3)(4)
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

print(next_moves(position_1, grid))
print(next_moves(position_2, grid))
print(next_moves(position_3, grid))
Example Output:

[(3, 1), (3, 3), (2, 2)]
Example 1 Explanation: The cell to the left, right, and one up from (3, 2) all have value 1 and thus
are safe next moves. The cell one down from (3, 2) has value 0 and is thus unsafe.

[(0, 3), (1, 3)]
Example 2 Explanation: The cell to the left and one down from (0, 4) have value 1 and thus are safe. 
The cells above and to the right are out of bounds of the grid. 

[]
Example 3 Explanation: All the cell up, left, right, and down of (0, 1) are either 0s or out of 
bounds. 
'''

# Understand: we are given an adjacency matrix, we are also given a position (row, col) and we want to determine a list of moves that are "safe"
#   - position is a tuple, and we want to return a list of tuples for the NEXT move
#   - we want to check up, left, right, and down and check if the value is 1 (safe) if it is 0 we continue to next move
#   - we save these values in a list and return at the end


# Match: BFS since we want the next level

# Plan: Create a result list, create a valid moves dict (up, left, right, and down), and use the dict to check moves

# - res = []
# - valid_moves = {
#   up: [0,1],
#   left: [-1, 0],
#   right: [1, 0],
#   down: [0, -1]
# } 
# loop through keys and perform the values on position
# make sure to keep contraints in mind

# we can move up if position[row][col] -> row != 0 col doesnt matter
# we can move left if position[row][col] -> row doesnt matter col != 0
# we can move right if position[row][col] -> row doesnt matter col != len(row) - 1
# we can move down if position[row][col] -> row != len(row) - 1 col doesnt matter

# if position + constraint == 1 add the res
# return 

# Implement:



# def next_moves(position, grid):
#     res = []

#     valid_moves = {
#         'up': (-1,0),
#         'left': (0, -1),
#         'right': (0, 1),
#         'down': (1, 0)
#     } 

#     pos_row, pos_col = position

#     if grid[pos_row][pos_col] != 1:
#         return []
    
#     for key, value in valid_moves.items():

#         val_row, val_col = value

#         match key:
#             case 'up':
#                 if pos_row != 0:
#                     if grid[pos_row + val_row][pos_col] == 1:
#                         res.append((pos_row + val_row,pos_col))
#             case 'left':
#                 if pos_col != 0:
#                     if grid[pos_row][pos_col + val_col] == 1:
#                         res.append((pos_row,pos_col+ val_col))
#             case 'right':
#                 if pos_col != len(grid[pos_row]) - 1:
#                     if grid[pos_row][pos_col + val_col] == 1:
#                         res.append((pos_row,pos_col + val_col))
#             case 'down':
#                 if pos_row != len(grid) - 1:
#                     if grid[pos_row + val_row][pos_col] == 1:
#                         res.append((pos_row + val_row, pos_col))

#     return res


def next_moves(position, grid):
    if not grid:
        return False
    
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    res = []

    if rows == 0 and cols == 0:
        return False
    
    directions = [(-1, 0),(1, 0),(0, -1), (0, 1)]

    for dr, dc in directions:
        r, c = position

        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 1:
                res.append((nr, nc))


    return res


grid = [
#   (0)(1)(2)(3)(4)
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)


print(next_moves(position_1, grid))
print(next_moves(position_2, grid))
print(next_moves(position_3, grid))

# Position 1:
# GRID[3][2] == 1

# Valid moves:
# UP: Grid[2][2] == 1       -> [3 - 1][2]  = [-1][0]
# LEFT: Grid[3][1] == 1     -> [3][2 - 1]  = [0][-1]
# RIGHT: Grid[3][3] == 1    -> [3][2 + 1]  = [0][+1]
# DOWN: Grid[4][2] != 1     -> [3 + 1][2]  = [+1][0]