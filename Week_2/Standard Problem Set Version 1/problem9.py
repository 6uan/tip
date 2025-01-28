'''
Problem 9: Stage Arrangement Difference Between Two Performances
You are given two strings s and t representing the stage arrangements of performers
in two different performances at a music festival, such that every performer occurs
at most once in s and t, and t is a permutation of s.

The stage arrangement difference between s and t is defined as the sum
of the absolute difference between the index of the occurrence of each performer
 in s and the index of the occurrence of the same performer in t.

Return the stage arrangement difference between s and t.

A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both
permutations of the list [1, 2, 3].

Hint: Absolute value function

def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
Example Usage:

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))
Example Output:

2
12

'''

#    0        1       2
# ["Alice", "Bob", "Charlie"]
#    1       0        2
# ["Bob", "Alice", "Charlie"]

# We want to find how far each performer is from their original position

# Use dict {person:index} for s1
# loop through t1 and for each i get the abs to the value of the dict
# keep this number in a var and return at the end 


def find_stage_arrangement_difference(s, t):
    diff = 0
    s_dict = {}

    for index, key in enumerate(s):
        s_dict[key] = index

    for index, key in enumerate(t):
        diff += abs(s_dict[key] - index)

    return diff

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))