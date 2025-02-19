'''
Problem 10: Timmy and Tommy
In a linked list, pointers can be redirected to any place in the list.

Using the linked list from Problem 9, create a new Node timmy with value "Timmy" and place it between tom_nook and tommy so the new linked list is tom_nook -> timmy -> tommy.

Example Usage:

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)
Example Output:

Tom Nook
Timmy
Timmy
Tommy
Tommy
None
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
timmy = Node("Timmy")
tom_nook.next = timmy
timmy.next = tommy 


print(tom_nook.value)       # Tom Nook
print(tom_nook.next.value)  # Timmy
print(timmy.value)          # Timmy
print(timmy.next.value)     # Tommy
print(tommy.value)          # Tommy
print(tommy.next)           # None