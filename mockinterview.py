'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
 
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:
Input: nums = [1,0,1,2]
Output: 3
'''

# Understand: Input: List Output: Int (longest conseq) || nums must increment by 1
# nums = [100,4,200,1,3,2] -> [1,2,3,4,100,200]

# Match: sliding window / 2 pointer first and sec

# Plan:
# nums = [100,4,200,1,3,2] -> [1,2,3,4,100,200]
#           l r
#  v v   v  v
# [1,2,3,4,100,200,201,202,203]

# value of i if it is i + 1
# value of j

# res list 

# Implement:

# Did not get solution

def consecutiveElements(nums):
    n = len(nums)

    if n == 0:
        return 0
    
    left = 0
    counter = 0

    nums = sorted(nums)

    for i in range(1, n):
        print(nums[i - 1] + 1, nums[i])
        if nums[i - 1] + 1 == nums[i]:
            counter += 1
          
    return counter


nums = [100,4,200,1,3,2]

print(consecutiveElements(nums)) # 4