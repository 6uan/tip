'''
Problem 4: Converting Flight Representations
Given a list of edges flights where flights[i] = [a, b] denotes that there exists a bidirectional flight (incoming and outgoing flight) from city a to city b, return an adjacency dictionary adj_dict representing the same flights graph where adj_dict[a] is an array denoting there is a flight from city a to each city in adj_dict[a].

def get_adj_dict(flights):
    pass
Example Usage:

'flights' graph diagram

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
Example Output:

{
    'Cape Town': ['Addis Ababa', 'Cairo'],
    'Addis Ababa': ['Cape Town', 'Lagos'],
    'Lagos': ['Cairo', 'Addis Ababa'],
    'Cairo': ['Cape Town', 'Nairobi'],
    'Nairobi': ['Cairo']
}

'''

# Understand: We are given a list of edges where each item represents a bidirectional flight [incoming, outgoing] -> [city a, city b] which means it can also be [city b, city a]. We want to convert this list of edges to an adjacency dictionary where the key is the source city, and the array reperesents a flight is either incoming or outcoming to each source


# Plan: We want to first create our dict. Then I wonder if we can treat our flights like a stack. We input:
# 
#  [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']] 

#  we pop
#  ['Cairo', 'Cape Town']

# now we iterate through these values: we first make 'Cairo' the key and create a ['Cape Town'] then we also use 'Cape Town' as key and create ['Cairo']

# now we can do this if we use a for loop with index, destination enumarate stack
# 0 'Cairo'
# 1 'Cape Town'
# if exists append, else
# dict[stack[0]] = stack[stack[1]]
# if exists append, else
# dict[stack[1]] = stack[stack[0]]


# We want           dict['Cape Town'] = ['Addis Ababa']
#                   dict[flight[0]] = [flight[1]]
        
# We also want      dict['Addis Ababa'] = ['Cape Town']
#                   dict[flight[1]] = [flight[0]]

# in both cases if we have an existing key append to the list


#               0              1
#           ['Cape Town', 'Addis Ababa'],
#           ['Cairo', 'Lagos'], 
#           ['Lagos', 'Addis Ababa'], 
#           ['Nairobi', 'Cairo'], 
#           ['Cairo', 'Cape Town']

# Implemenet:

def get_adj_dict(flights):
    flight_paths = {}

    
    for incoming, outgoing in flights:
        
        if incoming not in flight_paths:
            flight_paths[incoming] = []
        flight_paths[incoming].append(outgoing)
        
        if outgoing not in flight_paths:
            flight_paths[outgoing] = []
        flight_paths[outgoing].append(incoming)

    return flight_paths

flights = [ ['Cape Town', 'Addis Ababa'],
            ['Cairo', 'Lagos'], 
            ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], 
            ['Cairo', 'Cape Town']]

print(get_adj_dict(flights))

# {
#     'Cape Town': ['Addis Ababa', 'Cairo'],
#     'Addis Ababa': ['Cape Town', 'Lagos'],
#     'Lagos': ['Cairo', 'Addis Ababa'],
#     'Cairo': ['Cape Town', 'Nairobi'],
#     'Nairobi': ['Cairo']
# }

# {
#  'Cape Town': ['Addis Ababa', 'Cairo'],
#  'Addis Ababa': ['Cape Town', 'Lagos'],
#  'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
#  'Lagos': ['Cairo', 'Addis Ababa'],
#  'Nairobi': ['Cairo']}
#}