#!/usr/bin/python3
"""
A Function that queries the REDDIT API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ The function to query the API """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Darknught'}  # Custom User-Agent to avoid errors
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found.")
    else:
        print(None)
