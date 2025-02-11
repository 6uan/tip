from collections import deque
'''
Problem 2: Reveal Attendee List in Order
You are organizing an event where attendees have unique registration numbers. These numbers are provided in the list attendees.
You need to arrange the attendees in a way that, when their registration numbers are revealed one by one,
the numbers appear in increasing order.

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

# Understand:

# We are provided a list of unique ids
# We have to arrange the attendees (create new list or data structure)


# We take the top number from the list, 
# reveal it and remove it from the list (pop it from the queue?)
# is top (highest) or (head) of queue?
# 


def reveal_attendee_list_in_order(attendees):
    # [17,13,11,2,3,5,7] -> [17,13,11,7,5,3,2]
    attendees.sort(reverse=True)
    queue = deque()

    # 17
    # [no queue]
    # q.appendleft -> [17]

    # 13
    # [queue exist] -> q.appendleft(q.pop()) -> [17]
    # q.appendleft -> [13,17]

    # 11
    # [queue exist] -> q.appendleft(q.pop()) -> [17,13]
    # q.appendleft -> [11,17,13]

    # 7
    # [queue exist] -> q.appendleft(q.pop()) -> [13, 11, 17]
    # q.appendleft -> [7,13,11,17]

    # 5
    # [queue exist] -> q.appendleft(q.pop()) -> [17,7,13,11]
    # q.appendleft -> [5,17,7,13,11]

    # 3
    # [queue exist] -> q.appendleft(q.pop()) -> [11,5,17,7,13]
    # q.appendleft -> [3,11,5,17,7,13]

    # 2
    # [queue exist] -> q.appendleft(q.pop()) -> [13,3,11,5,17,7]
    # q.appendleft -> [2,13,3,11,5,17,7]

    for num in attendees:
        if queue:
            queue.rotate(1) # equivalent to queue.appendleft(queue.pop) or moving the last element to the front
        queue.appendleft(num)

    return queue



print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000])) 

