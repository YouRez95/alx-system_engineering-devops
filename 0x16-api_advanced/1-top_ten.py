#!/usr/bin/python3
"""
module that get the 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
      send the get request
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(
        url, headers={'User-Agent': 'test'}, allow_redirects=False)

    if response.status_code in range(300, 500):
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    for i in range(10):
        print(data[i].get('data', {}).get('title'))
