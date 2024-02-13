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
                     headers={'user-agent': "test"})

    if r.status_code != 200:
        return 0
    response = r.json()
    num_subscribers = response.get('data').get('subscribers')
    return num_subscribers
