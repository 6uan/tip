'''
Problem 1: NFT Name Extractor
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract
the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT,
and contains information such as the name, creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
for why you believe your solution has the stated time and space complexity.

def extract_nft_names(nft_collection):
    pass
Example Usage:

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
Example Output:

['Abstract Horizon', 'Pixel Dreams', 'Future City']
['Crypto Kitty', 'Galactic Voyage']
['Golden Hour']
'''


# Create a list to store names
# Iterate through nft_collection which has dicts -> O(n)
# Append to list -> O(1)

def extract_nft_names(nft_collection):
    result = []
    for nft_dict in nft_collection:
        result.append(nft_dict["name"])

    return result


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))