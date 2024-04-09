#!/usr/bin/python3
""" A Recursive function that queries REDDIT API and return list of titles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Return the list containing the titles for given subreddit."""
    hot_list = hot_list or []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    url += "&after={}".format(after) if after else ""

    headers = {"User-Agent": "Darknught"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list.extend(post["data"]["title"] for post in children)

        after = data.get("after")
        return recurse(subreddit, hot_list, after) if after else hot_list
    else:
        return None
