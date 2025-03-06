'''
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
Example Output:

3
4
'''

# Understand: Input: List of strings (suits) Output: Total number of suits in the list

# Plan: for iterative solution, create a counter, and use a for loop to increment suits
# for recursive solution, base case is if suits is empty return 0, else return 1 + recursive call with suits[1:]

# Implement

# These 2 solutions perform similar operations but take a very different approach in the iterative function we start
# from the "bottom up" and iterate until we reach the end to return the counter, however in the recursive solution
# we start from the end and break the problem into smaller and smaller subproblems until we hit our base case; only
# then will we construct our return by going through and returning all the values until we hit the first recursive call

def count_suits_iterative(suits):
    counter = 0

    for _ in suits:
        counter += 1

    return counter

def count_suits_recursive(suits):
    
    if not suits:
        return 0
    
    return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))