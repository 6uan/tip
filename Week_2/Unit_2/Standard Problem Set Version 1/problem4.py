"""

Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    pass
Example Usage:

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
Example Output:

{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}
"""

# Understand the problem: We take in two dicts with artists as keys and their set times as values. We need to find out
# if 2 key value pairs are the same add this key value pair to result dict.

# Plan a solution step-by-step: create result dict. keys = venue1.keys(), values = venue1.values() * 2 for venue 2. list1= zip(keys1, values1), list2 = zip(keys2, values2)
# make list1 a set using set(list1), iterate through list2 using a,b and check if value exits in our set. If it does match result[a] = b.
# return results


# Implement the solution:

def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}

    keys1, values1 = venue1_schedule.keys(), venue1_schedule.values()

    keys2, values2 = venue2_schedule.keys(), venue2_schedule.values()
    
    list1 = set(zip(keys1, values1))

    list2 = zip(keys2, values2)

    for a,b in list2:

        if (a,b) in list1:
            result[a] = b
        
    return result

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

