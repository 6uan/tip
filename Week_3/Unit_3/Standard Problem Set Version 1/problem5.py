'''
Problem 5: Content Cleaner
You want to make sure your posts are clean and professional. 

Given a string post of lowercase and uppercase English letters, you want to
remove any pairs of adjacent characters where one is the lowercase version
of a letter and the other is the uppercase version of the same letter. 

Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

def clean_post(post):
  pass
Example Usage:

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
Example Output:

post

s
'''

# "abBAcC" -> "a[bB]AcC" -> "aAcC" -> "[aA]cC" -> "cC" -> "[cC]" -> "" CLEAN

# Keep removing such pairs until the post is clean.

# Understand:
# We are given a string of chars where we need to remove char[i] + char[i + 1] 
# if they are the same char but different case

# Plan:

#             iterates                  stops early
#             [a, b]             ->    [b, B]          -> [a, A]
# "abBAcC" -> [a, b, B, A, c, C] -> [a, b, B, A, c, C] -> [a, A, c, C]

# since [b,B] matches our condition we remove from our list and start at 0 again

# 1st convert char to list to access indices
# modify list that will act as our return

# create our window which is just window[start: 2]
# if input is 1 char return early 

# Implement:


# def clean_post(post):
#     if len(post) <= 1:
#         return post
  
#     post_chars = list(post)
#     i = 0

#     while i < len(post_chars) - 1:
#         window = post_chars[i:i+2]

#         if window[0].lower() == window[-1] or window[0] == window[-1].lower():
#             post_chars.remove(window[0])
#             post_chars.remove(window[-1])
#             i = 0
#         else:
#             i += 1

#     return "".join(post_chars)

def clean_post(post):
    if len(post) <= 1:
        return post
    
    stack = []

    for char in post:
        if stack and stack[-1] != char and stack[-1].lower() == char.lower():
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)





print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 