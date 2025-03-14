'''
Problem 5: Heist
The legendary outlaw Robin Hood is looking for the target of his next heist. Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

def wealthiest_customer(accounts):
	pass
Example Usage:

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)
Example Output:

[0, 6]
[1, 10]
[0, 17]
'''

# Understand: We are given a m x n matrix where [i,j] is the amount of money the ith costumer has 
# We want to return i(index) of ith costumer and (w) is the sum of the [i,j] wealth of ith costumer

# Plan: create max wealth var to store wealth and compare to see which ith costumer is higher
# Loop through the matrix and store the sum of wealth and compare agiast max wealth
# We can also use a dict to store index


def wealthiest_customer(accounts):
    max_wealth = float('-inf')
    costumer_dict = {}
	
    for i in range(len(accounts)):
        wealth = sum(accounts[i])
        if wealth > max_wealth:
            max_wealth = wealth
            costumer_dict[i] = wealth
      
    for key, value in costumer_dict.items():
        if value == max_wealth:
            print([key,value])
            return [key, value]

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)

[0, 6]
[1, 10]
[0, 17]