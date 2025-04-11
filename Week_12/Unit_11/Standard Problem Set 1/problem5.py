'''
Problem 5: Zombie Spread
The zombie infection is spreading rapidly! Given a city represented as a 2D grid where 0 represents an obstacle where neither humans nor zombies can live, 1 represents a human safe zone and 2 represents a zone that has already been infected by zombies, determine how long it will take for the infection to spread across the entire city.

The infection spreads from each infected zone to its adjacent safe zones (up, down, left, right) in one hour. Return the number of hours it takes for all safe zones to be infected. If there are still safe zones remaining after the infection has spread everywhere it can, return -1.

def time_to_infect(grid):
    pass
Example Usage:

Example 1:`grid_1` showing infection spread every hour

grid_1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]]

grid_2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]]

grid_3 = [[0,2]]

print(time_to_infect(grid_1))
print(time_to_infect(grid_2))
print(time_to_infect(grid_3))
Example Output:

4
Example 1 Explanation: See image included above. 

-1
Example 2 Explanation: The safe zone in the bottom left corner (row 2, column 0) 
is never infected because infection only happens up, left, right, and down.

0
Example 3 Explanation: Since there are already no safe zones at minute 0, the answer is just 0
'''

from collections import deque


def time_to_infect(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    safe_zones = 0

    # append 2's to queue and 1's to safe zones

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                safe_zones += 1

    if safe_zones == 0:
        return 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    hour = -1

    while queue:

        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        safe_zones -= 1
                        queue.append((nr, nc))

        hour += 1


    return hour if safe_zones == 0 else -1


grid_1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]]

grid_2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]]

grid_3 = [[0,2]]

print(time_to_infect(grid_1))
print(time_to_infect(grid_2))
print(time_to_infect(grid_3))