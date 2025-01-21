'''
Problem 5: Concatenate

Write a function concatenate() that takes in a list of strings words and returns
a string concatenated that concatenates all elements in words.

def concatenate(words):
	pass
Example Usage

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
Example Output:

"vengeancedarknessbatman"
""
'''

# Understand the problem:

# We are given a list and we must concatenate the words together with no space
# We are expected to return a string of these words together
# If the list is empty return an empty string

# Plan a solution step-by-step:

# We can use a for loop to access every item in the list
# We can create an empty result string and append each item

# Implement the solution:

def concatenate(words):

    result = ""
    
    if len(words) == 0:
        return result   

    for word in words:
        result += word

    print(result)

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)