'''
Problem 3: Identify Popular Creators
You have been tasked with identifying the most popular NFT creators in your collection.
A creator is considered "popular" if they have created more than one NFT in the collection.

Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
for why you believe your solution has the stated time and space complexity.

def identify_popular_creators(nft_collection):
    pass
Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
Example Output:

['ArtByAlex']
['SpaceArt']
[]
'''

# For my solution I have time: O(n) and space O(n)
# Appending to my list will be O(1) and iterating through nft_collections will be O(n)
# For space, my list will grow 'n' creators if they have more than one NFT in the collection
# I use a set because every unique creator can be stored once at most. If it is in the set
# it means it has seen it before
# I use a list to store my results because we can append to it in O(1) time

def identify_popular_creators(nft_collection):
    seen = set()
    result = []

    for nft in nft_collection:
        if nft["creator"] in seen:
            result.append(nft["creator"])
        else:
            seen.add(nft["creator"])

    return result


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))