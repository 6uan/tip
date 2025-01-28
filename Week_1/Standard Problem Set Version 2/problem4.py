'''
Problem 4: Last

Implement a function get_last() that accepts a list of items items and
returns the last item in the list. If the list is empty, return None.

def get_last(items):
	pass
Example Usage

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
Example Output:

"black adam"
None
'''

# Understand the problem:

# We are given a list and we return the last item
# If our list is empty we turn None (not a string)
# Our list can have 0 to n items

# Plan a solution step-by-step:

# We can use the [-1] index to return the last item. 
# If our list is empty quickly return None

# Implement the solution:

def get_last(items):
    if len(items) == 0:
        return None # not shown in the terminal unless we print function

    print(items[-1]) 

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items) # "black adam"

items = []
get_last(items)

items = []
print(get_last(items)) # None