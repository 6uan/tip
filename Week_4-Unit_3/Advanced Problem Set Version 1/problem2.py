'''
Problem 2: Reveal Attendee List in Order
You are organizing an event where attendees have unique registration numbers. These numbers are provided in the list attendees. You need to arrange the attendees in a way that, when their registration numbers are revealed one by one, the numbers appear in increasing order.

The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:

Take the top registration number from the list, reveal it, and remove it from the list.
If there are still registration numbers in the list, take the next top registration number and move it to the bottom of the list.
If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
Return an ordering of the registration numbers that would reveal the attendees in increasing order.

def reveal_attendee_list_in_order(attendees):
  pass
Example Usage:

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  
Example Output:

[2,13,3,11,5,17,7]
[1,1000]
'''

