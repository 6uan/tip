'''
Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:

answer[i] == "HulkSmash" if i is divisible by 3 and 5.
answer[i] == "Hulk" if i is divisible by 3.
answer[i] == "Smash" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

def hulk_smash(n):
	pass
Example Usage:

n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)
Example Output:

["1", "2", "Hulk"]
["1", "2", "Hulk", "4", "Smash"]
["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]
'''

# Understand
# Match
# Prepare
# Implement
# Review
# Evaluate

# create our return list
# iterate our n till we reach n 
# for our current number check the 3 conditions
# add to our return list


def hulk_smash(n):
    
    result = []

    for number in range(1, n + 1):
        
        if number % 3 == 0 and number % 5 == 0:
            result.append("HulkSmash")
        elif number % 3 == 0:
            result.append("Hulk")
        elif number % 5 == 0:
            result.append("Smash")
        else:
            result.append(str(number))
            
    return result

print(hulk_smash(3))
print(hulk_smash(5))
print(hulk_smash(15))
