'''
Problem 10: Up and Down

Write a function up_and_down() that accepts a list of integers
lst as a parameter. The function should return the number of odd numbers
minus the number of even numbers in the list.

def up_and_down(lst):
	pass
Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4
'''

# Understand the problem:

# We want to return a single integer that subtracts the amount of even numbers from the odd numbers
# If there are no odd numbers we can go negative

# Plan a solution step-by-step:

# Initialize an even and odd counter at 0
# Iterate through the list and use a conditional statement to increment odd or even
# At the end return odd_count - even_count

# Implement the solution:

def up_and_down(lst):
    if not lst:
        return None
    
    odd_count = 0
    even_count = 0

    for number in lst:
        if number % 2 == 0:
            even_count += 1
        else: 
            odd_count += 1

    return odd_count - even_count

lst = [1, 2, 3]
print(up_and_down(lst)) # 1

lst = [1, 3, 5]
print(up_and_down(lst)) # 3

lst = [2, 4, 10, 2]
print(up_and_down(lst)) # -4