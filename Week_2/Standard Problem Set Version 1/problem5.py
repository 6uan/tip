"""

Problem 5: Best Set
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    pass
Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
Example Output:

SZA
Ethel Cain
Note: SZA and Ethel Cain would both be acceptable answers for the second example
"""

# Understand the problem: we take in vote dictionary and return most voted for person.

# Plan a solution step-by-step: freq = {}, iterate through values from votes, for every value check if it is in the dict, if it is, increment its freq
# value by 1 if it hasnt been seen before we initialize our artist using key to 1. then return max(freq.values())

# Implement the solution:

def best_set(votes):

    freq = {}

    for value in votes.values():

        freq[value] = 1 + freq.get(value, 0)
    
    list1 = list(zip(freq.values(), freq.keys()))
    print(list1)
    print(max(list1))
    return max(zip(freq.values(), freq.keys()))[-1]
    


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))