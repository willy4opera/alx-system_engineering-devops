#!/usr/bin/python3

"""This Function queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url_link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    Header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    result = requests.get(url_link, headers=Headers, allow_redirects=False)
    if result.status_code == 404:
        return 0
    Out_put = response.json().get("data")
    return Out_put.get("subscribers")
