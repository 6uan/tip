'''
Problem 2: There and Back
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j there also exists a flight from destination j to destination i. Return False otherwise.

def bidirectional_flights(flights):
    pass
Example Usage:

Example 1: flights1

'flights1' graph diagram

Example 2: flights2'flights2' graph diagram

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
Example Output:

True
False
'''

# Understand: We are given an adjancency list and we want to check if every flight is bidirectional

# Match: dict, for loop, and items()

# Implement:



def bidirectional_flights(flights):
    flight_paths = {}

    for index, path in enumerate(flights):
        flight_paths[index] = path

    for key, values in flight_paths.items():
        for val in values:
            if not key in flight_paths[val]:
                return False

    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
