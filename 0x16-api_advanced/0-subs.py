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
                     headers={'User-Agent': 'youness'}, allow_redirects=False)
    response = r.json()
    data = response.get('data', {})
    number_subscribers = data.get('subscribers', 0)
    return number_subscribers
