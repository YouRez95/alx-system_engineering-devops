#!/usr/bin/python3
"""
module that get the number of subscibers
"""
import requests


def number_of_subscribers(subreddit):
    """
      function that use the request module to send get request
    """

    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'youness'})
    response = r.json()
    num_subscribers = response.get('data', {}).get('subscribers', 0)
    return num_subscribers
