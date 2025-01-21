'''
Problem 2: Mad Libs

Write a function madlib() that accepts one parameter, a string verb.
The function should print the sentence: "I have one power. I never <verb>. - Batman".

def madlib(verb):
	pass
Example Usage

verb = "give up"
madlib(verb)

verb = "nap"
madlib(verb)
Example Output:

"I have one power. I never give up. - Batman"
"I have one power. I never nap. - Batman"
'''

# Understand the problem:

# Our function takes in a single string as an argument
# The argument replaces part of out print statement

# Plan a solution step-by-step:

# When we call madlib() the function should have a print() statement with an f string that replaces <verb>

# Implement the solution:

def madlib(verb):
	print(f"I have one power. I never {verb}. - Batman")

verb = "give up"
madlib(verb) # "I have one power. I never give up. - Batman"

verb = "nap"
madlib(verb) # "I have one power. I never nap. - Batman"