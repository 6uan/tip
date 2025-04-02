'''
Problem 7: Finding All Reachable Destinations II
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location start, write a function get_all_destinations() that uses Depth First Search (DFS) to return a list of all destinations that can be reached from start. The list should include both direct and connecting flights and should be ordered based on the order in which airports are visited in DFS.

def get_all_destinations(flights, start):
    pass
Example Usage:

'flights' graph diagram

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
Example Output:

['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 
'New York']
['Helsinki', 'Cairo', 'Reykjavik', 'New York']
'''

# Understand: We want to traverse through the nodes starting at the "start" using DFS
# For our adjacency dictionary
'''
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
'''

# We want to output for start = Beijing
# ['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 'New York']

# Plan:

# Create a stack = []
# Create a seen = set()

# Iterate starting on our start -> insert to stack ['Beijing']
# Pop from the 'Beijing' from stack and store as current
# check if in seen set if not add to result = ['Beijing',]

# Stack is now empty []
# loop through key values -> ['Mexico City', 'Helsinki'] and add each to stack
# iterate again

# ['Mexico City', 'Helsinki']
# Pop 


# Use recursion and explore the first path processed
# When we are at Beijing we have [Mexico City, Helsinki]
# Since Mexico City is first go down that path
# return call stack when we reach a "seen node" and explore next option

# Now we get Beijing -> Mexico City, Sydney, Tokyo, Since Toyko is in seen return 
# Now we explore Helsinki, Cairo, Reykavik and since Cairo is in seen return
# Now we explore New York, and since Helsinki is in seen return

# Base case is if node is in seen: return
# Recursion is pass in value from key value


'''
    Tokyo ←-→ Sydney --→ Beijing --→ Helsinki ←-→ Cairo
                ↑          ↙            ↑           ↑
                |        ↙              |           |
                |      ↙                ↓           ↓
            Mexico City             New York ←-→ Reykavik


'''


# Implement:

# def get_all_destinations(flights, start):
    
#     seen = set([start])
#     stack = [start]
#     result = []

#     while stack:
#         node = stack.pop()
#         result.append(node)

#         for flight in flights.get(node, []):
#             if flight not in seen:
#                 seen.add(flight)
#                 stack.append(flight)

#     return result

def get_all_destinations(flight, start):

    seen = set()
    result = []

    def helper(node):
        if node in seen:
            return
        seen.add(node)
        result.append(node)
        for neightbor in flight.get(node, []):
            helper(neightbor)
        
    helper(start)
    return result
        

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))

