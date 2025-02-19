'''
Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s catchphrase attribute directly.
Instead of allowing users to update their player directly, it is common to create setter methods
that users can call to update class attributes. This has a few different benefits, including allowing
us to validate data before updating our class instance.

Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase 
and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
		self.catchphrase = catchphrase
        self.furniture = []
	
	def set_catchphrase(self, new_catchphrase):
		pass
Example Usage:

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
Example Output:

Example 1:
Catchphrase Updated!
sweet dreams
Invalid catchphrase
sweet dreams
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(char.isalpha() or char.isspace() for char in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid catchphrase")

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

