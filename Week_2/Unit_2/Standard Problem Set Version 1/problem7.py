'''
Problem 7: Performances with Maximum Audience II
If you used a dictionary as part of your solution to max_audience_performances() in the previous problem, try reimplementing the function without using a dictionary. If you implemented max_audience_performances() without using a dictionary, try solving the problem with a dictionary.

Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?

def max_audience_performances(audiences):
    pass
Example Usage:

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
Example Output:

250
440
'''


# Understand the problem: 
# We want to return the highest number in the list, if we have a duplicate return the total of both sums


# Plan a solution step-by-step: 
# Create a frequency dict with the key being the audience size and value being how many times it appears
# Iterate throught they keys and use max() and sum() to calculate what to return


# Implement the solution:

def max_audience_performances(audiences):
    audience_dict = {}

    for key in audiences:
        if key in audience_dict:
            audience_dict[key] += 1
        else:
            audience_dict[key] = 1

    max_audience = max(audience_dict.keys())

    return max_audience * audience_dict[max_audience]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))