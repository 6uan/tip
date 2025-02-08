'''
Problem 6: Squared

Write a function squared() that accepts a list of integers numbers as a parameter
and squares each item in the list. Return the squared list.

def squared(numbers):
	pass
Example Usage

numbers = [1, 2, 3]
squared(numbers)
Example Output:

[1, 4, 9]
'''

# Understand the problem:

# We are given a list of integers and we must return the list with each value squared
# Can we handle negative numbers?
# Do we square in place or create a new list?
# What if our list is empty do we return None?

# Plan a solution step-by-step:

# We can use a for loop and iterate through each integer in the list
# We can also create a results list where we add each squared value
# We can square each value by multiplying it with itself

# Implement the solution:

def squared(numbers):
    if not numbers:
        return None
    
    results = []
    
    for number in numbers:
        results.append(number*number)

    return results

numbers = [1, 2, 3]
squared(numbers)

numbers = [1, 2, 3]
print(squared(numbers)) # [1, 4, 9]