'''
Problem 6: Smaller Than
Write a function smaller_than_current that accepts a list of integers nums and, for each element in the list nums[i], determines the number of other elements in the array that are smaller than it. More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer as a list.

def smaller_than_current(nums):
	pass
Example Usage:

nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)
Example Output:

[4, 0, 1, 1, 3]
[2, 1, 0, 3]
[0, 0, 0, 0]
'''

# Understand: We are given a list as input, for each int in this list we want to keep count of how many numbers of less than the ith number and store the number into a list
# [8, 1, 2, 2, 3] -> 8: 4 1:0 2:1 2:1 3:3

# Plan: We can use nested loops to check each individual number and compare it against current i
# if nums[i] is 8 we can check each number and increment if condition is found at the end store this res in a list and reset counter to 0

# Plan: Keep a frequency of each number key is nums[i] value is frequency
# Iterate through each key value pairs and sum the values that are lower than the key

# def smaller_than_current(nums):
#     res = []
	
#     for i in range(len(nums)):
#         counter = 0
#         for j in range(len(nums)):
#             if nums[j] < nums[i]:
#                 counter += 1
#         res.append(counter)

#     return res

def smaller_than_current(nums):
    sorted_nums = sorted(nums)
    num_count = {}

    for i, num in enumerate(sorted_nums):
        if num not in num_count:
            num_count[num] = i

    return[num_count[num] for num in nums]
        


nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

# nums = [6, 5, 4, 8]
# print(smaller_than_current(nums))

# nums = [7, 7, 7, 7]
# print(smaller_than_current(nums))

# [4, 0, 1, 1, 3]
# [2, 1, 0, 3]
# [0, 0, 0, 0]