"""
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to 
reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
  
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']


"""

# Understand:
#     Clarify - can input include empty strings? "", " "


# Plan:
#     - if len(comments) == 0: return comments
#     - stack = []
#     - result = []
#     - iterate through the comments and append to our stack
#     - ["Great post!", "Love it!", "Thanks for sharing."] len 3
#     - while stack:
#         result.append(stack.pop())
#     - return result


# Implement: 

def reverse_comments_queue(comments):
  if len(comments) == 0: return comments
  stack = []
  result = []
  for value in comments:
      stack.append(value)
      
  while stack:
      result.append(stack.pop())

  return result

  
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))