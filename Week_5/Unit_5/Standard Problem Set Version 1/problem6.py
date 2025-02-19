'''
Problem 6: Print Inventory
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity"
for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
class Villager():
    # ... methods from previous problems
    
    def print_inventory(self):
        # Implement the method here
        pass
Example Usage:

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.items = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
Example Output:

Inventory empty
acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2
'''


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.items = []

    def print_inventory(self):

        items_dict = dict()

        if len(self.items) == 0:
            print("Inventory empty")
        else:
            for item in self.items:
                if item in items_dict:
                    items_dict[item] += 1
                else:
                    items_dict[item] = 1

            output = ", ".join(f"{key}: {value}" for key, value in items_dict.items())
            print(output)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.items = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()