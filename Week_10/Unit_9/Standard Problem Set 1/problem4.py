'''
Problem 4: Maximum Tiers in Cake II
If you solved max_tiers() in the previous problem using a depth first search approach, reimplement your solution using a breadth first search approach. If you implemented it using a breadth first search approach, use a depth first search approach.

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

# Understand: We want to determine the depth of the binary tree using level order traversal. We are given a root and are asked to return an integer with the depth of the tree

# Match: Queue BFS

# Plan: We can use a deque to traverse through the binary tree
# queue = deque(root)
# while queue:
# node = queue.popleft()
# if node.left append left node to queue
# if node.right append right node to queue
# we must keep track of the depth somewhere in this logic
# return depth


"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""

# how do we determine we are in a new level ?
# when do we NOT append to levels

# levels = [[Chocolate], [Vanilla, Strawberry], [Chocolate, Coffee]]

# queue = ["Chocolate"] 
# append to levels -> [[Chocolate]]
# node = queue.popleft() -> Chocolate
# if node.left append left node to queue -> append Vanilla
# if node.right append right node to queue -> append Strawberry

# queue = ["Vanilla", "Strawberry"]
# append to levels -> [[Chocolate], [Vanilla, Strawberry]]
# node = queue.popleft() -> Vanilla
# if node.left append left node to queue -> skip
# if node.right append right node to queue -> skip

# queue = ["Strawberry"]
# DONT append to levels -> Stays at [Chocolate], [Vanilla, Strawberry]]
# node = queue.popleft() -> Strawberry
# if node.left append left node to queue -> Chocolate
# if node.right append right node to queue -> Coffee

# queue = ["Chocolate", "Coffee"]
# append to levels -> [[Chocolate], [Vanilla, Strawberry], [Chocolate, Coffee]]
# node = queue.popleft() -> Chocolate
# if node.left append left node to queue -> skip
# if node.right append right node to queue -> skip

# queue = ["Coffee"]
# DONT append to levels -> Stays at [[Chocolate], [Vanilla, Strawberry], [Chocolate, Coffee]]
# node = queue.popleft() -> Coffee
# if node.left append left node to queue -> skip
# if node.right append right node to queue -> skip

# queue = []

# return len(levels)

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

# The time complexity of this solution is O(n) because we must traverse through each node in the tree atleast once. We are using a queue to keep track of the nodes at each level, and we are returning the length of the result list which will be how many levels we have.

def max_tiers(cake):
    if not cake:
       return 0
   
    queue = deque([cake])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

        
    return len(result)
    

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""

cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))
