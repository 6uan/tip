'''
Problem 7: Foraging Berries
You've found a wild blueberry bush and want to do some foraging. However, you want to be conscious of the local ecosystem and leave some behind for local wildlife and regeneration. To do so, you plan to only harvest from branches where the number of berries is greater than threshold.

Given the root of a binary tree representing a berry bush where each node represents the number of berries on a branch of the bush, write a function harvest_berries(), that finds the number of berries you can harvest by returning the sum of all nodes with value greater than threshold.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
  pass
Example Usage:

"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))
Example Output:

38
Example 1 Explanation: 
- Nodes greater than 6: 8, 10, 20
- 8 + 10 + 20 = 38

0
Example 2 Explanation: No nodes greater than 30
'''

# Understand: We want to traverse the entire binary tree and get a running sum of nodes that have a greater value then threshold

# Match: BFS using queue

# Plan: Create a deque and insert the root
#  While we have queue traverse through each node and check the condition current > threshold if true add to sum else keep traversing 

# Implement:


# My time complexity for this function is O(n) where n is the number of nodes in the tree. I am traversing through each node in the tree to find the sum of nodes greater than threshold. I am using a BFS traversing each node through a queue where if the current node is above the threshold I add it to my total and add the left and right child nodes back into the queue

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):

    if not root:
        return
  
    queue = deque([root])
    total = 0

    while queue:
        current = queue.popleft()

        if current.val > threshold:
            total += current.val

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return total

"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))