'''
Problem 6: NFT Queue Processing
NFTs are added to a processing queue before they are displayed. The queue processes NFTs in a First-In, First-Out (FIFO) manner. Each NFT has a processing time, and you need to determine the order in which NFTs should be processed based on their initial position in the queue.

Write the process_nft_queue() function, which takes a list of NFTs. The function should return a list of NFT names in the order they were processed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def process_nft_queue(nft_queue):
    pass
Example Usage:

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))
Example Output:

['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
['Crypto Kitty', 'Galactic Voyage']
'''
from collections import deque

def process_nft_queue(nft_queue):

    queue = deque(nft_queue)
    result = []

    while queue:
        nft = queue.popleft()
        result.append(nft["name"])

    return result

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))