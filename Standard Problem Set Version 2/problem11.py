'''
Problem 11: Running Sum

Write a function running_sum() that accepts a list of integers superhero_stats
representing the number of crimes Batman has stopped each month in Gotham City.

The function should modify the list to return the running sum such that
superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). 

You must modify the list in place; you may not create any new lists as part of your solution.

def running_sum(superhero_stats):
	pass
Example Usage

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)
Example Output:

[1, 3, 6, 10]
[1, 2, 3, 4, 5]
[3, 4, 6, 16, 17]
'''

# Understand the problem:

# We have a function that takes in a list called superhero_stats
# This list contains integers and we are returning the same list with modified values
# For each index in the list we want to add the previous NEW value to the next
# [1,2,3,4] -> [1,3,6,10]
#  1 + 2 -> [1, 3] = [1,3,3,4]
#  3 + 3 -> [1, 3, 6] = [1,3,6,4]
#  6 + 4 -> [1, 3, 6, 10] = [1,3,6,10]

# Plan a solution step-by-step:

# First we iterate through the list and we must ensure we don't have an out of index error
# We are focused on the [i] and [i+1] indices

# We add the first index (1) with the 2nd index (2) and update the 2nd index (3)
# We then add the NEW 2nd index (3) with the 3rd index (3) and update the 3rd index (6)
# We then add the NEW 3rd index (6) with the 4th index (4) and update the 4th index (10)
# We reached the end so we return  

# Implement the solution:

def running_sum(superhero_stats):
    for i in range(len(superhero_stats) - 1):
        superhero_stats[i + 1] = superhero_stats[i] + superhero_stats[i + 1]
    return superhero_stats 


superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats)) # [1, 3, 6, 10]

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats)) # [1, 2, 3, 4, 5]

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats)) # [3, 4, 6, 16, 17]
