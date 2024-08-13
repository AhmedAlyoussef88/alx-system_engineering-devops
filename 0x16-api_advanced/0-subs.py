#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is provided, the function returns 0.
    
    :param subreddit: The name of the subreddit to query.
    :return: The number of subscribers or 0 if the subreddit is invalid.
    """
    # Define the URL to query
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set the User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Reddit API Client/0.1)'}
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response to get the number of subscribers
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0
            return 0
    except Exception:
        # In case of any exceptions, return 0
        return 0
