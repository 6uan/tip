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

# The time complexity of this solution is O(n) because we are making n recursive calls to find the highest strength
# the space complexity is O(n) because we are storing the recursive calls in the call stack
# We use a helper function to keep track of the max_strength and then return it at the end
# In the helper function we set our 0th index as the current_strength and then compare it to the max strength
# if it is greater we update the max_strength and then call the function again with the rest of the list
# if the list is empty we return the max_strength

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