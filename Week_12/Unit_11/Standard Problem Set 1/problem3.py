'''
Problem 3: List All Escape Routes
Having arrived at the safe haven, you are immediately put to work evaluating how many civilians can be evacuated to the safe haven. Given an m x n grid representing the city, return a list of tuples of the form (row, column) representing every starting position in the grid from which there exists a valid path of safe zones (1s) to the safe haven in the bottom-right corner of the grid.

If the starting cell has value 0, they are considered infected and cannot reach the safe haven.

def list_all_escape_routes(grid):
    pass
Example Usage:

grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

print(list_all_escape_routes(grid))
Example Output:

[(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]
'''

def list_all_escape_routes(grid):
    if not grid:
        return []
    
    rows = len(grid)
    cols = len(grid[0])

    if rows == 0 or cols == 0:
        return []
    
    sr, sc = rows - 1, cols - 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()

    def helper(r, c):
        stack = [(r, c)]
        visited.add((r, c))

        while stack:
            row, col = stack.pop()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))

    helper(sr, sc)

    return sorted(list(visited))


grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

print(list_all_escape_routes(grid))
# [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]