'''
Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their strengths, find the maximum strength using a recursive approach without using the max() function.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def strongest_avenger(strengths):
    pass
Example Usage:

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
Example Output:

100
Example 1 Explanation: The maximum strength among the Avengers is 100.

90
Example 2 Explanation: The maximum strength among the Avengers is 90.
'''

# Understand: we are given a list of integers and want to return the highest one

# Plan: we must keep track of the highest one we've seen


def strongest_avenger(strengths):
    
    def helper_function(strengths, max_strength):
        if not strengths:
            return max_strength
        
        current_strength = strengths[0]

        if current_strength > max_strength:
            max_strength = current_strength

        return helper_function(strengths[1:], max_strength)
    
    return helper_function(strengths, strengths[0])


print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))