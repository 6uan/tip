"""
Problem 2: Top Artists

Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. 

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


def get_artist_frequency(playlist):
	pass

Example Usage:

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)

Example Output:

{ "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}


"""

# Understand: Input: Linked List Head (Playlist) Output: Frequency Dictionary {"artist":"frequency_times_seen_in_playlist"}

# Plan: Create freq_dict traverse linked list playlist, and check current.artist if its in our dict += 1 the value if not set artist as key and value to 1 
# (first time seen in playlist)

# Implement:

class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next


def get_artist_frequency(playlist):
	
    freq_dict = {} # O(n) || O(set(current.artist))
    
    current = playlist # 1
    
    while current: # O(n)

        """
        freq_dict[current.artist] = 1 + freq_dict.get(current.artist, 0)
        """
		
        if current.artist in freq_dict: # 1
            freq_dict[current.artist] += 1 # 1
        else:
            freq_dict[current.artist] = 1 # 1
			
        current = current.next # 1

    return freq_dict # 1

playlist = SongNode("Saturn", "SZA", SongNode("Who", "Jimin", SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA"))))

# Saturn:SZA -> Who:Jimin -> Espresson:Sabrina Carpenter -> Snooze:SZA

print(get_artist_frequency(playlist)) # { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}
