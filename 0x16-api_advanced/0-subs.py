#!/usr/bin/python3
"""
number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    # Construct the URL for the subreddit's about page in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
