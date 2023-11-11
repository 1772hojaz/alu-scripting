#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
(total subsribers
"""

import json
import requests
import sys


def subscribers_num(subreddit):
    headers = {'User-Agent': 'Python:SubredditSubscriberCounter:v1.0(by /1772hojaz)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Making a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the response status code is 200 (OK), extract the number of subscribers
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
