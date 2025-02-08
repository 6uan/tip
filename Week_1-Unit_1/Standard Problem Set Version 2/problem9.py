'''
Problem 9: Odd

Write a function get_odds() that takes in a list of integers nums
and returns a new list containing all the odd numbers in nums.

def get_odds(nums):
	pass
Example Usage

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
Example Output:

[1, 3]
[]
'''

# Understand the problem:

# We take in one list and create a new one 
# We only want the odd numbers from the first list as our result
# Do we want them in the order we interate or in numeric?
# What if we get an empty list?
# What is the maximum number of odd numbers we can output?

# Plan a solution step-by-step:

# Create a new list for our result
# Iterate through the existing list and if number[i] % 2 == 1 it is odd
# Place this number in our new list and return at the end

# Implement the solution:

def get_odds(nums):
    result = []
    
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            result.append(nums[i])

    return result

nums = [1, 2, 3, 4]
print(get_odds(nums)) # [1,3]

nums = [2, 4, 6, 8]
print(get_odds(nums)) # []

