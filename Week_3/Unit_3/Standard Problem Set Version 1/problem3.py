
"""
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical,
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string,
use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
Example Output:

True
False
💡Hint: Two Pointer Technique

"""

# Understand:
#     Clarify:
#       - empty title return false
#       - we want to ignore cases, spaces, and punctuation
#       - does even or odd lengths matter? xccx vs xcx xxeexx still be true?


# Plan:
#   - intiatialize left and right pointer 
#   - use while to break out when left >= right
#   - check title[left] != title[right] if chars are equal left++ right-- else return false ?

#Implement:

def is_symmetrical_title(title):

    clean_text = title.lower().strip("!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~").replace(" ", "")
    
    left = 0
    right = len(clean_text) - 1

    while left <= right:
        if clean_text[left] != clean_text[right]:
            return False
        left +=1 
        right -= 1
        
    return True

#asantaatnasa
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))