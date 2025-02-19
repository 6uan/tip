'''
Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!".
For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

Example Usage:

print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 
Example Output:

Bones
Dog
yip yip
[]
'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, name):
        print(f"{self.name}: Hey there, {name}! How's it going, {self.catchphrase}!")

bones = Villager("Bones", "Dog", "yip yip")

print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 

bones.greet_player("Tram")