#!/usr/bin/python3

"""Here, we return a to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(sys.argv[1])).json()
    task = requests.get(link + "todos", params={"userId": sys.argv[1]}).json()

    finished = [t.get("title") for t in task if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(task)))
    [print("\t {}".format(c)) for c in finished]
