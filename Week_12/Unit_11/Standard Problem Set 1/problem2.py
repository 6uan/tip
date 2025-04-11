'''
Problem 2: Escape to the Safe Haven
You've just learned of a safe haven at the bottom right corner of the city represented by an m x n matrix grid. However, the city is full of zombie-infected zones. Safe travel zones are marked on the grid as 1s and infected zones are marked as 0s. Given your current position as a tuple in the form (row, column), return True if you can reach the safe haven traveling only through safe zones and False otherwise. From any zone (cell) in the grid you may move up, down, left, or right.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

def can_move_safely(position, grid):
    pass
Example Usage:

grid = [
    (0)(1)(2)(3)(4)
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

{
0:[0,2,3],
1:[0,1,2,3],
2:[2,3]
3:[0,2,3,4]

}


position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)

print(can_move_safely(position_1, grid))
print(can_move_safely(position_2, grid))
print(can_move_safely(position_3, grid))
Example Output:

True
Example 1 Explanation: Can follow the path (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
(2, 2) -> (3, 2) -> (3, 3) -> (3, 4)

True
Example 2 Explanation: Although we start in an unsafe position, we can immediately
arrive in a safe position and from there safely travel to the bottom right corner (3, 4).

False
'''

# Understand: Given a position we want to traverse until we reach index [len(grid[row]) - 1][len(grid) - 1] from position given



# Plan: Implement DFS with

#     (0)(1)(2)(3)(4)
#     [1, 0, 1, 1, 0], # Row 0
#     [1, 1, 1, 1, 0], # Row 1
#     [0, 0, 1, 1, 0], # Row 2
#     [1, 0, 1, 1, 1]  # Row 3
#                  ^
#              Safe Haven

# Given the position do DFS until we reach [len(grid[row]) - 1][len(grid) - 1]
# Base case is if [row][col] is already seen
# When we reach the safe haven position

# Recursive case is find the next_moves and for those nodes do the same 

# For [0][0] == 1
# our recursion will explore [0][1] and [1][0] for a == 1 
# if it is == 1 we will perform the same recursion for that [row][col] too


#  Implement:

# The time complexity for this solution is O(N * M), since in the worst case scenario we will traverse to each grid cell in the grid. 
# The space complexity is also O(N * M), because we are using a set that can store each grid cell and the stack can also grow to hold every cell; our rows and cols variables are constant as well as our sr, sc "safe haven" values. We also have a list that holds every direction we can traverse (top, down, left, right)


def can_move_safely(position, grid):
    if not grid:
        return False
    
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    sr, sc = rows - 1, cols - 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # DFS (Iterative)
    def helper(r, c):
        stack = [(r, c)]
        visited.add((r, c))

        while stack:
            row, col = stack.pop()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        if (nr, nc) == (sr, sc):
                            return True
                        visited.add((nr, nc))
                        stack.append((nr, nc))
 
        return False

    r, c = position

    return helper(r, c)

    
grid = [
#   (0)(1)(2)(3)(4)
    [1, 0, 1, 1, 0], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 1, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)

print(can_move_safely(position_1, grid))
print(can_move_safely(position_2, grid))
    # return false if no grid

    # define our row and col length
    # define our directional movement

    # create a DFS helper that takes in position and appends to stack

    # base case
    # when we
    # once our r, c is == sr, sc we can return True

print(can_move_safely(position_3, grid))