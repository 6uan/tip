'''
Problem 7: NaNaNa Batman!

Write a function nanana_batman() that accepts an integer x and prints the string
"nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
	pass
Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
Example Output:

"nananananana batman!"
"batman!"
'''

# Understand the problem:

# The function takes in a single int parameter (x) which is responsible for how many "na" we want
# to prefix "batman!" If a 0 value is passed in we simply return "batman!"
# What happens if we put in a negative value?
# Is there a maximum amount of "na" that can be reached?

# Plan a solution step-by-step:

# I will first check if the value passed in is 0 if it is I can quickly return just batman!
# My approach will be to create a variable called prefix that is set to ""
# I will loop through the range of x and append "na" to my prefix until we break out
# at the end I will concatenate prefix and "batman!"

# Implement the solution:

def nanana_batman(x):
    if x == 0:
        return "batman!"
    
    prefix = ""

    for _ in range(x):
        prefix += "na"

    return prefix + " " + "batman!"


x = 6
print(nanana_batman(x))

x = 0
print(nanana_batman(x))