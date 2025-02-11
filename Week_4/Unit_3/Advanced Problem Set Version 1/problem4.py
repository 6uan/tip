'''
Problem 4: Rearrange Guests by Attendance and Absence
You are organizing an event, and you have a 0-indexed list guests of even length,
where each element represents either an attendee (positive integers) or an absence (negative integers).
The list contains an equal number of attendees and absences.

You should return the guests list rearranged to satisfy the following conditions:

Every consecutive pair of elements must have opposite signs, indicating that each attendee is followed by an absence or vice versa.
For all elements with the same sign, the order in which they appear in the original list must be preserved.
The rearranged list must begin with an attendee (positive integer).
Return the rearranged list after organizing the guests according to the conditions.

def rearrange_guests(guests):
  pass
Example Usage:

print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 
Example Output:

[3,-2,1,-5,2,-4]
[1,-1]
'''

# Understand:
# We must have a list that alternates > 0 and < 0 between each ith item
# We must preserve the order the items come in 
# Must begin with positive item

# Plan:
# Create a left pointer at 0, right pointer at left + 1
# While left < right
#  L R
# [3,1,-2,-5,2,-4]
# L > 0: move right once
# R > 0: move right until we find < 0
# Swap L and R
# When we swap move L and R once

#    L R                    L R
# [3,1,-2,-5,2,-4] -> [3,-2,1,-5,2,-4]

