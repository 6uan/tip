'''
Problem 4: Largest Safe Zone
With more and more civilians evacuating to the safe haven, you need more space! Given a m x n grid of the city where 1s represent safe zones and 0s represent infected zone, return the area of the largest group of safe zones in the grid. Any zone grid[i][j] has an area of 1 and its connected zones are the adjacent cells up, down, left, and right of it.

def largest_safe_zone(grid):
    pass
Example Usage:

grid = [
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

print(largest_safe_zone(grid))
Example Output:

8
Explanation: There are two groups of connected 1s. The group beginning in Row 0 has size 4.
The group beginning in Row 2 has size 8, so we return 8. 
'''


def largest_safe_zone(grid):
    # empty grid edge case
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    visited = set()
    max_group_size = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def helper(r, c):
        stack = [(r, c)]
        visited.add((r, c))
        size = 0

        while stack:
            row, col = stack.pop()
            size += 1

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))

        return size
    

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                group_size = helper(row, col)
                max_group_size = max(max_group_size, group_size)

    return max_group_size


grid = [
    [0, 0, 0, 1, 1], # Row 0
    [0, 0, 0, 1, 1], # Row 1
    [1, 1, 1, 0, 0], # Row 2
    [1, 1, 1, 1, 0], # Row 3
    [0, 0, 0, 1, 0]  # Row 4
]

print(largest_safe_zone(grid))

