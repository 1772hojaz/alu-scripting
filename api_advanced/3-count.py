#!/usr/bin/python3
"""
Python script that returns the number of subscribers
for a given subreddit 
"""
import sys
import requests
import re


def count_words(subreddit, word_list, after='', counts={}):
    if after is None:  # Base case for recursion
        sorted_counts = sorted([(word.lower(), count) for word, count in counts.items()], key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')
        return

    if after == '':
        for word in word_list:
            counts[word.lower()] = 0

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    headers = {'User-Agent': 'python:count_words:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] += len(re.findall(r'\b' + re.escape(word_lower) + r'\b', title))
        after = data['data']['after']
        count_words(subreddit, word_list, after, counts)
    except Exception as e:
        return

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
