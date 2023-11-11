#!/usr/bin/python3
"""this module contains a function that returns the number"""
import requests


def number_of_subscribers(subreddit):
    """this function returns the number of subscribers"""
    reddit_url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    header = {
        'User-agent': 'Mozilla/5.0'
        '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(reddit_url,
                            headers=header
                            )

    if response.status_code == 200:
        data = response.json()['data']
        subs = data['subscribers']
        return subs
    return 0
