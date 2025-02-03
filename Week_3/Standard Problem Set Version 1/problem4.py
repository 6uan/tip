
"""
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 

To analyze the impact of certain strategies, you decide to square each engagement rate and
then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares
of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.


Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]
"""

# def engagement_boost(engagements):
#     squared_engagements = []
    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     squared_engagements.sort(reverse=True)
    
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
    
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result

def engagement_boost(engagements):
    
    results = [0] * len(engagements)

    left = 0
    right = len(engagements) - 1
    position = len(engagements) - 1

    while left <= right:
        engagements_left = engagements[left] * engagements[left]
        engagements_right = engagements[right] * engagements[right]

        if engagements_left < engagements_right:
            results[position] = engagements_right
            right -= 1
        else:
            results[position] = engagements_left
            left += 1

        position -= 1

    return results

    #   L             R
    # [-4, -1, 0, 3, 10]

    # check -4 against 10 for ABS
    # 10 is higher so we square number 
    # add to results at a position index that starts at end


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))