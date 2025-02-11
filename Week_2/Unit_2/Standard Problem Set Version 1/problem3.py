'''
Problem 3: Ticket Sales
A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    pass
Example Usage:

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
Example Output:

4500

'''

# Understand the problem: 
# We want to output the sum of all the values in the dictionary. 
# In the current scenario it would be all the ticket sales that are of int type

# Plan a solution step-by-step: 
# define a sum variable, iterate through the dict values for each value add to the sum, return the sum 

# Implement the solution:


def total_sales(ticket_sales):
    sum = 0

    for value in ticket_sales.values():
        sum += value

    return sum

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))