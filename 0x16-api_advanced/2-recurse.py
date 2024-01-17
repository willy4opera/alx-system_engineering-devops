#!/usr/bin/python3
""" Recursive function that queries the Reddit API """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """     Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    global after
    Head = {'User-Agent': 'xica369'}
    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    passed_params = {'after': after}
    querry_data = requests.get(link, headers=Head, allow_redirects=False,
                               params=passed_params)

    if querry_data.status_code == 200:
        nxt_d = querry_data.json().get('data').get('after')
        if nxt_d is not None:
            after = nxt_d
            recurse(subreddit, hot_list)
        title_lst = querry_data.json().get('data').get('children')
        for title in title_lst:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
