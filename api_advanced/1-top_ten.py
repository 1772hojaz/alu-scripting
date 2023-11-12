#!/usr/bin/python3
"""this module returns the titles of the top 10 hot posts"""
import requests
import sys


def top_ten(subreddit):
    """Function that queries the Reddit API."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))
    else:
        print(None)
        