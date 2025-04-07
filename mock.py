'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# Understand: input: s output: true or false
#  - we want to remove whitespaces and symbols (only keep letters and numbers)
#  - ""

# Plan: take our string and sanitize it 
# first we remove white space, and symbols, while keeping letters and numbers
# convert the string into a list
# create 2 pointers -> one at the beggining of the list and one at the end
# while loop and while left pointer <= right pointer
# if s[l] == s[r] we can continue and increment left and decrement right
# s[l] != s[r]: False

# Implement:

def palindrome(s):
    
    clean_text = ''.join(char for char in s if char.isalnum())

    s_sanitized = list(clean_text.lower())
    left = 0
    right = len(s_sanitized) - 1

    while (left <= right):
        if s_sanitized[left] != s_sanitized[right]:
            return False
        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(palindrome(s))

