#!/usr/bin/python3
""" A Function that queries the Reddit API and returns number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Darknught"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    Data = response.json().get("data")
    return Data.get("subscribers")
