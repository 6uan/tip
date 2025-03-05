'''
Problem 5: Calculating the Power of the Fantastic Four
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. Write a recursive function that calculates the power of 4 raised to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def power_of_four(n):
    pass
Example Usage:

print(power_of_four(2))
print(power_of_four(-2))
Example Output:

16
Example 1 Explanation: 2 to the 4th power (4 * 4) is 16. 
16
Example 2 Explanation: -2 to the 4th power is 1/(4 * 4) is 0.0625.
'''

# Understand: we want to take an int input and raise it to the 4th power, it it is negative we want to have it over 1

# Plan: determine base cases
# input (2) -> 16
# 2 * 2 * 2 * 2
# if n < 0 
# return 1 / recursive power
# else return recursive * 4 

# Implement:


def power_of_four(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 1 / power_of_four(-n)
    
    return 4 * power_of_four(n - 1)

print(power_of_four(2))
print(power_of_four(-2))