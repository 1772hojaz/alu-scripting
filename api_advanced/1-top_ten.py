#!/usr/bin/python3
"""this module returns the titles of the top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
