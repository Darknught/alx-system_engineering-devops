#!/usr/bin/python3
""" A Function that queries the Reddit API and returns number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """The Function to query the API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyGuy'}  # a custom User-Agent to avoid errors

    # Prevent following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
