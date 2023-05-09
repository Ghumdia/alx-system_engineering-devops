#!/usr/bin/python3
"""Makes a query for the subscriber counts for a sub reddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscriber counts for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    x = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if x.ok:
        data = x.json()
        try:
            sub_count = int(data['data']['subscribers'])
            return(sub_count)
        except KeyError:
            return(0)
    else:
        return(0)
