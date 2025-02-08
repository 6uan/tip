"""
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, 
such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, 
and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.

def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False
"""

# Understand:
#    Clarify - each opening char should have correct closing char ex. (). 
#              limited to ()[]{} assume no other char input.
#              for result stack we want to make sure its empty becuase if it isn't the input isn't balanced.

# Plan:
#     - check length of input incase we return early.
#     - we want to use a dict to store characters were looking for. {')':'('}
#     - create a stack
#     - iterate through input and store only opening brackets in the stack ['('] -> if we see a closing bracket (use dict) of same type ')' we can pop off stack
#     - once we finish return if len(stack): return False else return True
#     - return True if len(stack) == 0 else False

# Implement:
def is_valid_post_format(posts):

    if len(posts) <= 1:
        return False
    
    close_to_open = {
      ')': '(',
      ']': '[',
      '}': '{'
    }

    stack = []

    for char in posts:
        if char in close_to_open and stack:
            if close_to_open[char] == stack[-1]:
                stack.pop()
        else:
            stack.append(char)

    return True if len(stack) == 0 else False
    

print(is_valid_post_format("{([)]}"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
