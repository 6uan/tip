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

# The time complexity is O(1) because we are only evaluating three nodes in the tree: the root and its two children. The time complexity does not depend on the size of the tree, as it is always a fixed number of nodes. The function uses switch case to match the root operation and calculate the yield.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def calculate_yield(root):
    if isinstance(root.val, int):
        return root.val
    
    left_node = calculate_yield(root.left)
    right_node = calculate_yield(root.right)

    match root.val:
        case '+':
            return left_node + right_node
        case '-':
            return left_node - right_node
        case '*':
            return left_node * right_node
        case '/':
            return left_node / right_node if right_node != 0 else "Divide by zero error!"
        case _:
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