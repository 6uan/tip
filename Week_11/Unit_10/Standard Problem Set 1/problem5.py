'''
Problem 5: Find Center of Airport
You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with n nodes where each node represents a terminal in the airport labeled from 1 to n. You want to find the center terminal in the airport where the pilots' lounge is located.

Given a 2D integer array terminals where each terminal[i] = [u, v] indicates that there is a path (edge) between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.

def find_center(terminals):
    pass
Example Usage:

'terminals1' graph diagram

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))
Example Output:

2
1
'''

# Understand: we want to find the center of the "airport" in other words find the center node that connects to every other node

# Plan:
# My center node is present in EVERY edge path
# Need to make sure when we loop through each list to make sure that value is present
# Take the first list and get the values in a set
# check every other list against these values

# terminals1 = [[1,2],[2,3],[4,2]]

# Turn arr into a adjacency dict

# {
#   1: [2]
#   2: [1, 3, 4]
#   3: [2]
#   4: [2]
# }

def find_center(terminals):

    terminal_paths = {}

    for u, v in terminals:
            
        if u not in terminal_paths:
            terminal_paths[u] = []
        terminal_paths[u].append(v)
            
        if v not in terminal_paths:
            terminal_paths[v] = []
        terminal_paths[v].append(u)


    for key, value in terminal_paths.items():
        if len(value) == len(terminals):
            return key

       

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

    
    