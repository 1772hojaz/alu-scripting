#!/usr/bin/python3
"""this module returns the titles of the top 10 hot posts"""
import requests
import sys


def top_ten(subreddit):
    """this function returns the titles of the top 10 hot posts"""
    subreddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(subreddit_url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children')
            for post in data:
                print(post.get('data').get('title',))
        else:
            print(None)
    except request.RequestException as e:
        print(None)

if __name__ == "__main__":
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)
    else:
        top_ten(sys.argv[1])
    