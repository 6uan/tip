'''
Problem 8: Flower Fields
You're looking for the perfect bloom to add to your bouquet of flowers. Given the root of a binary tree representing flower options, and a target flower flower, return True if the bloom you are looking for each exists in the tree and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
  pass
Example Usage:

"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))
Example Output:

True
False
'''

# Understand: We want to find if a target node exist in our tree.
#   - Is the tree sorted in any order?
#   - How can I reach the target as fast as possible

# Match: BFS or DFS traversal checking if node exist

# Plan: We can create a queue for BFS and traverse tree until we find node if not we turn false


# My time complexity is O(n) where n is the number of nodes in the tree. I am visiting each node to check if the node is equal to the target node.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    if root is None:
        return False
    
    if root.val == flower:
        return True
    
    return find_flower(root.left, flower) or find_flower(root.right, flower)


"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))