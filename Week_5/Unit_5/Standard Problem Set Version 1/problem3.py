'''
Problem 3: Update Catchphrase
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".

Example Usage:

print(bones.greet_player("Samia"))
Example Output:

Bones: Hey there, Samia! How's it going, ruff it up!
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


bones.greet_player("Tram") # catchphrase: "yip yip"

bones.catchphrase = "ruff it up"

bones.greet_player("Samia") # catchphrase: "ruff it up"