'''
Problem 12: Print List
Write a function print_list() that takes in the head of a linked list and returns a string
linking together the values of the list with the separator "->".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

Example Usage:

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))
Example Output:

Isabelle -> Saharah -> C.J.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def print_list(head):

    current_node = head
    output = []

    while current_node:
        output.append(current_node.value)
        current_node = current_node.next


    return " -> ".join(output)

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))