'''Problem 1: Words Containing Character
Write a function words_with_char() that accepts a list of strings words and a character x. Return a list of indices representing the words that contain the character x. The returned list may be in any order.

def words_with_char(words, x):
	pass
Example Usage:

words = ["batman", "superman"]
x = "a"
words_with_char(words, x)

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
words_with_char(words, x)

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
words_with_char(words, x)
Example Output:

[0, 1]
[0, 2]
[]
'''

# if words list is empty return empty list 
# create an empty list called results

# iterate through the string words (keep track of indices)
# for each word check if it has 'x' char
# if it has 'x' char add index to result list
# else continue iterating

# return our results list

def words_with_char(words, x):
    ...
    if not words:
        return []
    
    results = []

    for index in range(len(words)):
        if x in words[index]:
            results.append(index)

    return results


# words = ["batman", "superman"]
# x = "a"
# print(words_with_char(words, x))

# words = ["black panther", "hulk", "black widow", "thor"]
# x = "a"
# print(words_with_char(words, x))

# words = ["star-lord", "gamora", "groot", "rocket"]
# x = "z"
# print(words_with_char(words, x))