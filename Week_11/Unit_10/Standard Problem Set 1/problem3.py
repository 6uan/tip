'''
Problem 3: Finding Direct Flights
Given an adjacency matrix flights of size n x n where each of the n nodes in the graph represent a distinct destination and n[i][j] = 1 indicates that there exists a flight from destination i to destination j and n[i][j] = 0 indicates that no such flight exists. Given flights and an integer source representing the destination a customer is flying out of, return a list of all destinations the customer can reach from source on a direct flight. You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of source.

def get_direct_flights(flights, source):
    pass
Example Usage:

'flights' graph diagram

flights = [
               0  1  2  3
            0 [0, 1, 1, 0],
            1 [1, 0, 0, 0],
            2 [1, 1, 0, 1],
            3 [0, 0, 0, 0]]


    0 <----> 1
    ^     /|
    |   /
    v
    2 -----> 3

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
Example Output:

[0, 1, 3]
[]
'''

# Understand: We are given a n by b matrix where each n nodes in the graph is a distinct destination 
# if n[i][j] = 1 there exist a flight from destination i to destination j
# what does source mean if it is 2 does it mean entire index 2 row and index 2 column?


# brute force solution
def get_direct_flights(flights, source):
    result = []

    for node, destinations in enumerate(flights):
        if node == source:
            for index, flight in enumerate(destinations):
                if flight == 1:
                    result.append(index)
        
    return result


flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))