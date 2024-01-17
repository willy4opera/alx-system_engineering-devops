#!/usr/bin/python3
"""Prints hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    Head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(link, headers=Head, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(data.get("data").get("title")) for data in results.get("children")]
