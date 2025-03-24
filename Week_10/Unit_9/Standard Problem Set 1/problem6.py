'''
Problem 6: Icing Cupcakes in Zigzag Order
You have rows of cupcakes represented as a binary tree cupcakes where each node in the tree represents a cupcake. To ice them efficiently, you are icing cupcakes one row (level) at a time, in zig zag order (i.e., from left to right, then right to left for the next row and alternate between).

Return a list of the cupcake values in the order you iced them.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def zigzag_icing_order(cupcakes):
    pass
Example Usage:

"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))
Example Output:

['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
'''

# Understand: We are given a binary tree and we want to print the values out in "zig-zag" format. Each time we move down a level we switch the order in which we traverse. We print our depth 1 (root), and for depth 2 with traverse our right children to left. At depth 3 we traverse our left children to right. We switch each time

# Match: BFS, queue, for loop maybe a boolean 

# Plan: We implement a BFS as
# while queue:
#   level = [] <- keeps track of each level
#   for _ in range(len(queue)): <- traverse left to right
#   node = queue.popleft()
#   if node.left -> queue.append(node.left)   
#   if node.right -> queue.append(node.right)  

# we also want to keep track of each level and a return list for the end
# On EVEN levels we traverse backwards

# Implement:

from collections import deque

class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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

def zigzag_icing_order(cupcakes):
    if not cupcakes: 
        return cupcakes
    
    queue = deque([cupcakes])
    result = []

    zigzag = False

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if zigzag:
            result.extend(reversed(level))
        else:
            result.extend(level)

        zigzag = not zigzag
     
    return result

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))

"""
            Chocolate                   Depth: 1
           /         \
        Vanilla       Lemon             Depth: 2
       /              /    \
    Strawberry   Hazelnut   Red Velvet  Depth: 3 
"""

# v ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']

"""
            Chocolate                   Depth: 1
           /         \
        Lemon        Vanilla            Depth: 2
       /              /    \
    Strawberry   Hazelnut   Red Velvet  Depth: 3 
"""
