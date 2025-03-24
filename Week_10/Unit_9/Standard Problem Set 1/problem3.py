'''
Problem 3: Maximum Tiers in Cake
You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    pass
Example Usage:

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))
Example Output:

3
'''

# Understand: We want the maximum depth of our binary tree

# Match: Use DFS / recursion

# Plan: We want to recurse through the binary tree and keep track of the depth with an accumulator at the end we return the max depth between both sides
"""
        Chocolate               -> max_tiers(cake, depth=None) -> recurse down left and right if not cake return None else increment depth by 1?
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""

# Base case: if not cake: means hit a nonexisting node return and build through recursive stack

# def max_tiers(cake):
#     pass

# Implement:
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


def max_tiers(cake):
    if not cake:
        return 0
    
    left_side = max_tiers(cake.left)
    right_side = max_tiers(cake.right)

    return  1 + max(left_side, right_side)

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""

# max_tiers(Chicolate)
# left_side = 1 + max(tiers(Vanilla))
# max(tiers(Vanilla))
# return 0 -> 1 + 0 = 1

# right_side = 1 + max(tiers(Strawberry))
    
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))