'''
Problem 7: Post Compare
You often draft your posts and edit them before publishing.

Given two draft strings draft1 and draft2, return true if they are equal
when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will remain empty.

def post_compare(draft1, draft2):
  pass
Example Usage:

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
Example Output:

True
True
False
'''

# Understand:
# We are given 2 string inputs
# Each input is a combination of alpha chars and '#'
# '#' is considered a backspace so "ab#c" is "ac"
# We must find is after removing the characters backspaced if both strings are the same
# If there are more '#' then alpha chars string remains empty

# Plan:
# Create a function that takes in a singular string and uses a stack to perform the backspaces
# stack = []
# for char in string
# if char = '#' -> pop from stack
# else append to stack
# return final word using .join
# in original function return processed_string1 == processed_string2

# Implement:
def post_compare(draft1, draft2):
    return handle_backspace(draft1) == handle_backspace(draft2)

def handle_backspace(draft):
    if len(draft) == 0:
        return draft
    
    stack = []

    for char in draft:
        if char == '#':
            if not stack:
                continue
            else:
                stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 