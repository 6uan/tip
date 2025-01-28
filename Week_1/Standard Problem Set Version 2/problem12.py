'''
Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n
elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
	pass
Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
Example Output:

['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]
'''

# Understand the problem:

# We are given a list that is divisible by 2 and
# includes both string and integers and we want to shuffle it
# We want the first item to be next to the middle + 1
# Do we do it in place or create a new list?
# What if our list is odd?

# Plan a solution step-by-step:

# Create a new list called result
# We can create a variable that calculates the midpoint by using len(cards) // 2

# input:
#    0         1     2  3   4    5
# ['Joker', 'Queen', 2, 3, 'Ace', 7]

# output: 
#    0      3    1       4     2  5
# ['Joker', 3, 'Queen', 'Ace', 2, 7]

# Iterate through the list by index and stop at midpoint
# We start the list by placing the first index and append [midpoint + 1]
# When we reach the midpoint we know we would have visited every item
# Return the shuffled list

# Implement the solution:


# Understand the problem:

# Plan a solution step-by-step:

# Implement the solution:

def shuffle(cards):
	result = []
	midpoint = len(cards) // 2
	
	for i in range(midpoint):
		result.append(cards[i])
		result.append(cards[midpoint + i])
	
	return result

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards)) # ['Joker', 3, 'Queen', 'Ace', 2, 7]

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards)) # [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

cards = [10, 10, 2, 2]
print(shuffle(cards)) # [10, 2, 10, 2]