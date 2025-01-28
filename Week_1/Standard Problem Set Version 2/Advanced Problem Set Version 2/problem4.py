'''
Superman is doing yet another good deed, using his power of flight
to distribute meals for the Metropolis Food Bank. He wants to distribute meals
in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains
meals[i] meals. There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, write a function
minimum_boxes() that returns the minimum number of boxes needed to redistribute
the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes.

def minimum_boxes(meals, capacity):
	pass
Example Usage:

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)
Example Output:

2
4
'''

# Understand the problem ->
#    meals = [1, 3, 2]       -> [1,1,2,3], [1,2,_], [_], [_,_,_,_,_], [_,_] -> 2 boxes full only (partially empty rest)
# capacity = [4, 3, 1, 5, 2] -> [_,_,_,_], [_,_,_], [_], [_,_,_,_,_], [_,_]

#    meals = [5, 5, 5]    -> [1,2], [3,4,5,1], [2,3], [4,5,1,2,3,4,5] -> 4 boxes full
# capacity = [2, 4, 2, 7] -> [_,_], [_,_,_,_], [_,_], [_,_,_,_,_,_,_]

# Plan a solution step-by-step

# maybe sort meals in order and capacity in reverse
# start at first index of both 
# decrement the value in capacity
# when i'th capacity hits 0 or goes under 0, increment global min box save the remainder and iterate to next

# Implement the solution

#    meals = [1, 2, 3]      
# capacity = [5, 4, 3, 2, 1]

# 1st iteration          | 2nd iteration         | 3rd iteration 
# meals = 1              | meals = 2             | meals = 3
# capacity = 5           | capacity = 4          | capacity = 2
# capacity - meals = r   | capacity - meals = r  | capacity - meals = r
# 5 - 1 = 4              | 4 - 2 = 2             | 2 - 3 = -1 -> next box
#
#                                                | meals = 1
#                                                | capacity = 4
#                                                | 4 - 1 = 3 -> no more meals return 2

def minimum_boxes(meals, capacity):
    sorted_meals = sorted(meals)
    sorted_capacity = sorted(capacity, reverse=True)
    counter = 0
    left1 = 0
    left2 = 0

    while sorted_meals: # [1,2,3]
        if sorted_meals[left1] > sorted_capacity[left2]:
            sorted_capacity[left2] - sorted_meals[left1]
            sorted_meals.popleft()
           
    return counter 

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals,capacity))