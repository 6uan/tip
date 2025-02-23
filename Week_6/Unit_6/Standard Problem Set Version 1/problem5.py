'''
Problem 5: Looped
Given the head of a linked list playlist_head that may contain a cycle,
use the fast and slow pointer method to return the length of the cycle.
If the list does not contain a cycle, return 0.

Evaluate the time and space complexity of your solution.
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
	pass
Example Usage:

Linked list of four songs, with fourth song pointing to second song

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
Example Output:

3
'''

# Understand: We want to see if our linkedlist has a cycle if it does return the length of the cycle (inclusive) else return 0

# Plan: We can adapt the code from problem4.py (slow fast pointer) and when we find our cycle 
# we run a pointer until we reach the node we saw before


#     slow:   1            2           3           4
#     fast:   1            3           2           4
#           [song 1] -> [song 2] -> [song 3] -> [song 4]
#                          ^                       | 
#                          |_______________________| 

# Our cycle is song 2 -> song 3 -> song 4 which is length of 3
# When we find song 2 both our fast and slow pointer will be at it
# Increment slow pointer and counter until we reach it again

class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
	
    fast, slow = playlist_head, playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # when we find our cycle start
        if slow == fast:
            counter = 1 
            slow = slow.next
            # iterate slow pointer until we get back to the fast
            while slow != fast:
                slow = slow.next
                counter+=1

            return counter

    return 0        

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))