'''
Problem 5: Count the Tree Leaves
You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! Given the root of a binary tree representing your oak tree, count the number of leaf nodes in the tree. A leaf node is a node that does not have any children.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):
    pass
Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))
Example Output:

3
1
'''

# Understand: We want to return the number of leaf nodes (nodes that have node.left and node.right ponting to none)

# Match: Traversing Tree, Recursion

# Plan:
#   - Base Case: When our node has no left or right value return 1
#   - Recursion: Explore left and right nodes till we hit the base case

# count_leaves(root, sum=0)
# if not root.left and not root.right:
#    sum += 1
#    return
# left_node = recurse left
# right_node = recurse right


# Implement: 

# The time complexity is O(n) where n is the number of nodes in the tree. I am traversing the entire tree to count only the nodes that don't have a left or right child, using an accumulator to keep track of the sum.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root, sum=None):

    if sum == None:
        sum = 0

    if not root.left or not root.right:
        sum += 1
        return sum

    return count_leaves(root.left, sum) + count_leaves(root.right, sum)


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))