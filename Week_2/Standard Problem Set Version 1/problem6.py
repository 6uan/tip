'''
Problem 6: Performances with Maximum Audience
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

Return the combined audience size of all performances in audiences with the maximum audience size.

The audience size of a performance is the number of people who attended that performance.

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
# Create a return variable (this will handle duplicates), create a max_audience variable set to ('inf')
# Sort the list then iterate through the list and find the highest audience
# Iterate through list again and add all the max audiences that are equal
# Return result if its not 0 (means theres duplicates) else return max_audience (singular)

# Implement the solution:

def max_audience_performances(audiences):
    result = 0
    max_audience = float('-inf')
    sorted_audiences = sorted(audiences)

    for i in sorted_audiences:
        if i > max_audience:
            max_audience = i

    for i in sorted_audiences:
        if i == max_audience:
            result += i

    return result if result != 0 else max_audience

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))