#!/usr/bin/python3
"""
module that get the 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
      send the get request
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    response = requests.get(
        url, allow_redirects=False, headers={'User-Agent': 'test'})

    if response.status_code in range(300, 500):
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    for post in data:
        print(post.get('data', {}).get('title'))
