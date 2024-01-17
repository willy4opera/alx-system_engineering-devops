#!/usr/bin/python3
"""Here, we count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Here, we print the counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    Head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    fetch_data = requests.get(link, headers=Head, params=params,
                            allow_redirects=False)
    try:
        results = fetch_data.json()
        if fetch_data.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for num in results.get("children"):
        title = num.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda Keyval: (-Keyval[1], Keyval[0]))
        [print("{}: {}".format(numx, numy)) for numx, numy in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
