'''
Problem 5: Can Fulfill Order
At your bakery, you organize your current stock of baked goods in a binary tree with root inventory where each node represents the quantity of a baked good in your bakery. A customer comes in wanting a random assortment of baked goods of quantity order_size. Given the root inventory and integer order_size, return True if you can fulfill the order and False otherwise. You can fulfill the order if the tree has a root-to-leaf path such that adding up all the values along the path equals order_size.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    pass
Example Usage:

"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))
Example Output:

True
Example 1 Explanation: 5 + 4 + 11 + 2 = 22

False
'''

# Understand: we want to reach a target sum (root to leaf path) from our binary tree. We can either return true or false 

# Match: DFS / recursion 

# Plan: 
#   - our function takes in (tree, target)
#   - we must keep track of current path target
#   - if current path == target return True
#   - if we reach leaf node return False

from collections import deque

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

# This solution is O(n) because at worst we will have to traverse each node in the tree once. We are using a recursive function to traverse the tree and check if the sum of the path equals the target. We store the current sum in an accumulator and check if it equals the target. If we reach a leaf node and the sum does not equal the target, we return False. 

def can_fulfill_order(inventory, order_size, curr_sum=0):

    if curr_sum == order_size:
        return True

    if not inventory:
        return False
        
    curr_sum += inventory.val

    return can_fulfill_order(inventory.left, order_size, curr_sum) or can_fulfill_order(inventory.right, order_size, curr_sum)    


quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))

"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

print(can_fulfill_order(baked_goods, 13))
print(can_fulfill_order(baked_goods, 19))