#!/usr/bin/python3

"""Importing required modules"""
from pip._vendor import requests

def number_of_subscribers(subreddit):
    x = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json", headers={'User-Agent': 'Mozilla/5.0'}
:Wq

