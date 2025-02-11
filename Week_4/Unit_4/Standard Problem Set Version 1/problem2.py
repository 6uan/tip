'''
Problem 2: NFT Collection Review
You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery.
One of your tasks is to review and debug the code that extracts the names of NFTs from the collection.
A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

Task:

Review the provided code and identify the bug(s).

Explain what the bug is and how it affects the output.

Refactor the code to fix the bug(s) and provide the correct implementation.

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names += nft["name"]
    return nft_names
Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
Example Output:

['Abstract Horizon', 'Pixel Dreams']
['Golden Hour']
[]
'''

# Errors:
# When we iterate through nft_collection we are accessing dictionaries within a list
# List do not function with "+=" they use .append() to add new items to it

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        # nft_names += nft["name"]
        nft_names.append(nft["name"]) # modified 
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

