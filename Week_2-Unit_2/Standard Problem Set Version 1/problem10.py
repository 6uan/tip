'''
Problem 10: VIP Passes and Guests
You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing the guests you have at the music festival. Each character in guests is a type of guest you have. You want to know how many of the guests you have are also VIP pass holders.

Letters are case sensitive, so "a" is considered a different type of guest from "A".

Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count.
def num_VIP_guests(vip_passes, guests):
    pass
Example Usage:

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))
Example Output:

3
0
'''

# Vip pass list has a string which can be split to chars 'aA' -> 'a' 'A' 
# We want to search for these chas in our guests and count how many times they appear case sensitive


def num_VIP_guests(vip_passes, guests):
    char_bank = set(vip_passes)
    count = 0

    for char in guests:
        if char in char_bank:
            count += 1

    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))
