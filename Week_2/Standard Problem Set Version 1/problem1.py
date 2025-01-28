"""

Problem 1: Festival Lineup
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    pass
Example Usage:

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

Example Output:

{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}


"""

# Understand the problem: Given artist list and set time list where each ith artist and set time must be connected via key-value pair
# if artist list empty or set list empty, return empty dict 

# Plan a solution step-by-step: Create dict, iterate through artists using range, i iterator will map the set time to the artist, set will
# be the value, and artist will be the key, return result

# Implement the solution:

def lineup(artists, set_times):
    
    if not (artists or set_times):
        return {}
    
    results = {}

    for i in range(len(artists)):
        # map each artist to their respective set time
        results[artists[i]] = set_times[i]
    
    return results
    
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

print(lineup(artists1, set_times1))

artists2 = []
set_times2 = []

print(lineup(artists2, set_times2))