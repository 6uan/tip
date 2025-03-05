'''
Problem 7: Counting Vibranium Deposits
In Wakanda, vibranium is the most precious resource, and it is found in several deposits. Each deposit is represented by a character in a string (e.g., "V" for vibranium, "G" for gold, etc.)

Given a string resources, write a recursive function count_deposits() that returns the total number of distinct vibranium deposits in resources.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def count_deposits(resources):
    pass
Example Usage:

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
Example Output:

5
2
Example 2 Explanation: There are two characters "V" in the string "VXVYGA", 
therefore there are two vibranium deposits in the string.
'''


def count_deposits(resources):
    if not resources:
        return 0
    
    if resources[0] == 'V':
        return 1 + count_deposits(resources[1:])
    else:
        return count_deposits(resources[1:])

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))