"""
Problem 2: Planning App
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    pass
Example Usage:

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
Example Output:

{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}"""

# Understand the problem: Were accepting a string artist, and given a dict festival_schedule where we want to know whether
# that artist is mapped in our festival_schedule, and if they are we want to return their value, otherwise if the artist doesn't
# exist we return a dict -> {'message': 'Artist not found'}.

# Plan a solution step-by-step: iterate festival schedule using key, value festival_schedule.items() then we want to check
# if "artist" is present -> return value, after the loop ends if we dont return we can assume the artist isn't present therefore
# we return -> {'message': 'Artist not found'}

# Implement the solution:

def get_artist_info(artist, festival_schedule):
    
    for key, value in festival_schedule.items():
        if key == artist:
            return value
    
    return {'message': 'Artist not found'}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))