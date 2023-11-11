#!/usr/bin/python3
"""
Python script that returns the number of subscribers for a given subreddit
to the Reddit API
"""
import requests
import sys


def subscribers_num(subreddit):
   """
   Recursive function that queries the Reddit API and returns a list
   containing the titles of all hot articles for a given subreddit
   args:
   subreddit: the name of the subreddit
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
