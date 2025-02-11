'''
Problem 8: Find Closest NFT Values
Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of NFT values and a budget,
you need to find the two NFT values that are closest to the given budget: one that is just below or equal to the budget
and one that is just above or equal to the budget. If an exact match exists, it should be included as one of the values.

Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget,
and returns the pair of the two closest NFT values.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_closest_nft_values(nft_values, budget):
    pass
Example Usage:

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
Example Output:

(7.2, 9.0)
(6.3, 7.8)
(2.5, 4.0)
'''

# we want to find closest 2 values
# we can set closest_under and check for highest value that is also < budget
# we can set closest_over and check for lowest value that is also > budget
# we can set equal value that is None and also append value if it is ==
# store result as a tuple


# For this solution we have O(n) time and O(1) space
# We will iterate through our values n times
# We perform conditional checks on the values
# For our space we are storing a fixed amount of variables
# closest_under, closest_over, and equal_value which will
# be reassigned during the for loop

def find_closest_nft_values(nft_values, budget):
    closest_under = float('-inf')
    closest_over = float('inf')
    equal_value = False

    for value in nft_values:
        if value > closest_under and value < budget:
            closest_under = value

        if value < closest_over and value > budget:
            closest_over = value

        if value == budget:
            equal_value = True

    return (closest_under, budget, closest_over) if equal_value else (closest_under, closest_over)



nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
