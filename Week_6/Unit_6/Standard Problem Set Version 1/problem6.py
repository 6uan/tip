'''
Problem 6: Volume Control
You are working as an engineer normalizing volume levels on songs. Given the head of a singly linked list
with integer values song_audio representing volume levels at different points in a song, return the number
of critical points. A critical point is a local minima or maxima.

The head and tail nodes are not considered critical points. *
A node is a local minima if both the next and previous elements are greater than the current element
A node is a local maxima if both the next and previous elements are less than the current element
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why
you believe your solution has the stated time and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
	pass
Example Usage:

song_audio linked list

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))
Example Output:

3
Explanation: There are three critical points:
- The third node is a local minima because 1 is less than 3 and 2.
- The fifth node is a local maxima because 5 is greater than 2 and 1.
- The sixth node is a local minima because 1 is less than 5 and 2.
'''

# Understand: Can local min/max be the head or the tail ? NO

# Define the prev, current, and next nodes
# Our prev will be the head
# Our curr will be head.next
# Our next will be curr.next
# 
# We will iterate while we have curr and curr.next
# For each curr node we will have conditional statements to check
# A node is a local minima if both the next and previous elements are greater than the current element -> curr node < both prev and next
# A node is a local maxima if both the next and previous elements are less than the current element -> curr node > both prev and next
# We can store this in a counter

# Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

# 
#        1      2     (3)     4     (5)    (6)     7
#       [5] -> [3] -> [1] -> [2] -> [5] -> [1] -> [2]

# prev should be head
# current should be head.next
# next should be current.next

#        p      c      n
#        1      2     (3)     4     (5)    (6)     7
#       [5] -> [3] -> [1] -> [2] -> [5] -> [1] -> [2]


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
    if not song_audio.next:
        return 0
    
    prev = song_audio
    current = song_audio.next
    next = current.next
    counter = 0

    while current and current.next:
        if prev.value < current.value > next.value:
             counter += 1
        elif prev.value > current.value < next.value:
             counter += 1

        prev = prev.next
        current = current.next
        next = next.next


    return counter

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))