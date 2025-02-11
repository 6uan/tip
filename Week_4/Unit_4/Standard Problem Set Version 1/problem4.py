'''
Problem 4: NFT Collection Statistics
You want to provide an overview of the NFT collection to potential buyers.
One key statistic is the average value of the NFTs in the collection. 
However, if the collection is empty, the average value should be reported as 0.

Write the average_nft_value function, which calculates and returns the average value of the NFTs in the collection.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale
for why you believe your solution has the stated time and space complexity.

def average_nft_value(nft_collection):
    pass
Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))
Example Output:

5.7
9.15
0
'''

# For my solution I have time: O(n) and space O(1)
# My average variable will sum values O(1) iterated from my for loop which is O(n)
# For space, I have O(1) because we are not storing more data we are simply summing and storing length (fixed variables)


def average_nft_value(nft_collection):
    average = 0
    n = len(nft_collection)

    if n == 0:
        return average
    
    for nft in nft_collection:
        average += nft["value"]

    return average / n


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))