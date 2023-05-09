#!/usr/bin/python3
"""Importing required modules"""
import requests


def top_ten(subreddit):
    """Filters the first 10 hot title posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    x = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if x.ok:
        data = x.json()
        try:
            i = 0
            while i <= 9:
                hot_count = data['data']['children'][i]['data']["title"]
                print(hot_count)
                i += 1
        except IndexError:
            print('None')
    else:
        print('None')
