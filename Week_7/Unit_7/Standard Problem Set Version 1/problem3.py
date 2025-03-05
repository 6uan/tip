'''
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of unique suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

Example Output:

3
2
'''

# Understand: we are given a list of string and we want to only increment a counter if the string is unique

# Plan: for out iterative approach we can create a set and then use a for loop to check if the string is in the seen set, else add to set and increment counter or len of set
# for recursive solution we can return 0 + recursive call and the base case will be if suit is in a set and list is empty

# Implement:

def count_suits_iterative(suits):
    seen = set()
    counter = 0

    for suit in suits:
        if suit not in seen:
            counter += 1
            seen.add(suit)
        else:
            continue

    return counter


def count_suits_recursive(suits):
    if not suits:
        return 0
    
    unique, rest = suits[0], suits[1:]

    removed_unique = [suit for suit in rest if suit != unique]

    return 1 + count_suits_recursive(removed_unique)

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
