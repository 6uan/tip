'''
Problem 8: Find Itinerary
You are a traveler about to embark on a multi-leg journey with multiple flights to arrive at your final travel destination. You have all your boarding passes, but their order has gotten all messed up! You want to organize your boarding passes in the order you will use them, from your first flight all the way to your last flight that will bring you to your final destination.

Given a list of edges boarding_passes where each element boarding_passes[i] = (departure_airport, arrival_airport) represents a flight from departure_airport to arrival_airport, return an array with the itinerary listing out the airports you will pass through in the order you will visit them. Assume that departure is scheduled from every airport except the final destination, and each airport is visited only once (i.e., there are no cycles in the route).

def find_itinerary(boarding_passes):
    pass
Example Usage:

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))
Example Output:

['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
'''

# Understand: We are given a list of edges and we want to find which path visits each vertice atleast once. Since we are given that departure is scheduled from every airport except the final destination we can just traverse each starting node until our result = len(boarding_pass) + 1

# Plan:
#   - We want to iterate through the list and for each [0]th vertice use DFS traversal 
#   - We must keep track of seen and result

# Implement:

def find_itinerary(boarding_passes):

    flight_map = {}
    seen = set()

    for origin, destination in boarding_passes:
        flight_map[origin] = destination
        seen.add(destination)

    start = None
    for origin in flight_map:
        if origin not in seen:
            start = origin
            break

    result = [start]
    while start in flight_map:
        next = flight_map[start]
        result.append(next)
        start = next

    return result


boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))
