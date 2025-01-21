'''
Problem 8: Find the Villain

Write a function find_villain() that accepts a list crowd and a
value villain as parameters and returns a list of all indices
where the villain is found hiding in the crowd.

def find_villain(crowd, villain):
	pass
Example Usage

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
Example Output:

[1, 4, 6]
'''

# Understand the problem:

# We are tasked with finding the items in a list of items
# For each item we find that is matching we store the index in a result list
# What if nothing matches?
# What if we have an empty crowd and a non-empty villain or vise versa
# Is the villain case sensitive?

# Plan a solution step-by-step:

# We can first create a result list to store the indices
# We can loop through the crowd using index (crowd[i]) and at each index check if
# the string matches the villain
# If it matches add to list else continue iterating
# Return the list 

# Implement the solution:

def find_villain(crowd, villain):
    results = []

    for i in range(len(crowd)):
        if crowd[i] == villain:
            results.append(i)

    return results

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
print(find_villain(crowd, villain)) # [1, 4, 6]