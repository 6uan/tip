'''
Problem 6: Finding All Reachable Destinations
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or connecting flights with layovers. The list should be provided in ascending order by number of layovers required.

def get_all_destinations(flights):
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

['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']

'''

from collections import deque

def get_all_destinations(flights, source):
    result = []    

    queue = deque([source])
    seen = set([source])
    result.append(source)

    while queue:
        for _ in range(len(queue)):
            flight = queue.popleft()

            for path in flights.get(flight, ""):
            
                if path not in seen:
                    result.append(path)
                    seen.add(path)
                    queue.append(path)
            
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