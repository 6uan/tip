'''
Problem 3: Arrange Event Attendees by Priority
You are organizing a large event and need to arrange the attendees based on their priority levels.
You are given a 0-indexed list attendees, where each element represents the priority level of an attendee,
and an integer priority that indicates a particular level of priority.

Your task is to rearrange the attendees list such that the following conditions are met:

Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
Return the attendees list after the rearrangement.

def arrange_attendees_by_priority(attendees, priority):
  pass
Example Usage:

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 
Example Output:

[9,5,3,10,10,12,14]
[-3,2,4,3]

'''

# Understand: 
# We are given an attendees list that has priority level of each guest
# We are also given an int that indicates a level of priority
# We must rearrange the list to meet 3 conditions:
#   - every ith item < priority must be before ith item > priority
#   - every ith item == priority must be between conditions above
#   - order must be preserved from left to right ?


# Plan:
# Create left pointer at 0
# Create right pointer at len(attendees)
# Create i at 0
# While i <= R
# p = 10
#                          R
#                    L               
#                          I                    
# Keep track of [9,5,3,10,10,14,12]

# We will check every item for
# item < p
#   item[i], item[L] = item[L], item[i]
#   left += 1
#   i += 1
# item > p:
#   item[i], item[R] = item[R], item[i]
#   right -= 1
# item == p:
#   i += 1


# Implement

def arrange_attendees_by_priority(attendees, priority):
    left = 0
    n = len(attendees)
    i = 0

    # first pass sets attendess[i] < priority 
    while i < n:
        if attendees[i] < priority:
            attendees[left], attendees[i] = attendees[i], attendees[left]
            left += 1
        i += 1


    mid = left
    i = mid

    # second pass sets attendees[i] == priority
    while i < n:
        if attendees[i] == priority:
            attendees[mid], attendees[i] = attendees[i], attendees[mid]
            mid += 1
        i += 1
        

    # due to first 2 passes the end will always be in order
    return attendees
    

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 