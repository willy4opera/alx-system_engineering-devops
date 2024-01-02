#!/usr/bin/python3

"""Script to exports to-do list information
for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    UserId = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    User = requests.get(link + "users/{}".format(UserId)).json()
    UserName = User.get("username")
    Task = requests.get(link + "todos", params={"userId": UserId}).json()

    with open("{}.json".format(UserId), "w") as jsonfile:
        json.dump({UserId: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": UserName
            } for t in Task]}, jsonfile)
