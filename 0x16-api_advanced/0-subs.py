"""Importing required modules"""
from pip._vendor import requests

def number_of_subscribers(subreddit):
    x = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json", headers={'User-Agent': 'Mozilla/5.0'})
    if x.ok:
        data = x.json()
        try:
            sub_count = data['data']['subscribers']
            print(sub_count)
        except KeyError:
            print(0)
    else :
        print(0)
