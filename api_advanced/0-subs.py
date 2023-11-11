#!/usr/bin/python3

"""
This module provides a function `subscribers_num` that queries the Reddit API to determine the number
of subscribers for a specified subreddit. If the subreddit is valid, it returns the total number of subscribers.
In case of an invalid subreddit or an error in the request, it returns 0.

The module is designed to be run as a script, taking the subreddit name as a command-line argument.
"""

import requests
import sys


def subscribers_num(subreddit):
    """
    Query the Reddit API to get the number of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    headers = {'User-Agent': 'Python:SubredditSubscriberCounter:v1.0 (by /u/1772hojaz)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers = subscribers_num(subreddit_name)
        print(f"{subscribers}")

