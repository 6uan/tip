'''
Problem 2: Calculating Yield
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
The root has a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  pass
Example Usage:

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))
Example Output:

12
'''

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# def calculate_yield(root):
#     if not root:
#         return None
  
#     queue = deque([root])

#     while queue:
#         current_node = queue.popleft()

#         if current_node.val == '+':
#             return current_node.left.val + current_node.right.val
#         elif current_node.val == "-":
#             return current_node.left.val - current_node.right.val
#         elif current_node.val == "*":
#             return current_node.left.val * current_node.right.val
#         elif current_node.val == "/":
#             return current_node.left.val / current_node.right.val
#         else:
#             return "Not a valid operation!"

def calculate_yield(root):
    if isinstance(root.val, int):
        return root.val
    
    left_node = calculate_yield(root.left)
    right_node = calculate_yield(root.right)

    if root.val == '+':
        return left_node + right_node
    elif root.val == "-":
        return left_node - right_node
    elif root.val == "*":
        return left_node * right_node
    elif root.val == "/":
        return left_node / right_node
    else:
        return "Not a valid operation!"  
  


apple_tree1 = TreeNode("+", TreeNode(7), TreeNode(5))
apple_tree2 = TreeNode("-", TreeNode(7), TreeNode(5))
apple_tree3 = TreeNode("*", TreeNode(7), TreeNode(5))
apple_tree4 = TreeNode("/", TreeNode(7), TreeNode(5))
apple_tree5 = TreeNode("=", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree1)) # 7 + 5 = 12
print(calculate_yield(apple_tree2)) # 7 - 5 = 2
print(calculate_yield(apple_tree3)) # 7 * 5 = 35 
print(calculate_yield(apple_tree4)) # 7 / 5 = 1.4
print(calculate_yield(apple_tree5)) # Not a valid operation