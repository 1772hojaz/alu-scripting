#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import sys
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    headers = {'User-Agent': 'python:recurse:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data['data']['children']
        hot_list += [post['data']['title'] for post in posts]
        after = data['data']['after']

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception as e:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
