#!/usr/bin/python3
"""
module that get all hot posts for a given subreddit by recursive
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
      send the get request
    """
    def make_request(after=""):
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
        response = requests.get(
            url, allow_redirects=False, headers={'User-Agent': 'test'})
        if response.status_code in range(300, 500):
            return None
        data = response.json().get('data')
        after = data.get('after')
        posts = data.get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if after is None:
            return
        return make_request(after)

    make_request("")
    if len(hot_list) == 0:
        return None
    return hot_list
