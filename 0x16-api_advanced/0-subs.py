#!/usr/bin/python3
"""
module that get the number of subscibers
"""
import requests


def number_of_subscribers(subreddit):
    """
      function that use the request module to send get request
    """
    if not subreddit or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'user-agent': "test"})
    response = r.json()
    num_subscribers = response.get('data', {}).get('subscribers', 0)
    return num_subscribers
