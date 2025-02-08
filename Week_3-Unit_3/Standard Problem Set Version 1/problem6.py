'''
Problem 6: Post Editor
You want to add a creative twist to your posts by reversing the order of characters
in each word within your post while still preserving whitespace and the initial word order.
 Given a string post, use a queue to reverse the order of characters in each word within the sentence.

def edit_post(post):
  pass
Example Usage:

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
Example Output:

tsooB ruoy tnemegegna htiw esehT spit
kcehC tuo ym tseval golv

'''

# Understand:
# We want to take in a string (words of a sentence) and for each word reverse the word and keep the same order
# We want to keep char cases and white spaces in the sentence

# Plan:
# Break the sentence into a list of words where whitespaces will be added later
# Use a queue process each word and perform the reversing
# Append each reversal into a result list 
# Build the string again

# "Boost your engagement with these tips" -> ["Boost","your","engagement","with","these","tips"]
# ["Boost","your","engagement","with","these","tips"] -> Queue gets "Boost"
# We reverse "Boost" and end with "tsooB" in our new list ["tsooB",]
# Wait for next input until Queue is empty
# When we have ["tsooB","ruoy","tnemegegna","htiw","eseht","spit"]
# Build the string by adding a space between every item except [-1]
# Return tsooB ruoy tnemegegna htiw eseht spit

#Implement:

from collections import deque

def edit_post(post):
    post_list = post.split()
    result = []
  
    queue = deque(post_list)

    while queue:
        current_word = queue.popleft()
        result.append(current_word[::-1])

    return " ".join(result)


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 