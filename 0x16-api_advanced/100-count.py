#!/usr/bin/python3
"""
A Recursive function that queries the Reddit api, parses the title and
prints sorted count of given keywords "case sensitive and delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Returns the list of titles of all hot articles."""
    counts = counts or {}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    url += "&after={}".format(after) if after else ""

    headers = {"User-Agent": "Darknught"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
