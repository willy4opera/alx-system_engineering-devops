#!/usr/bin/python3

"""The python script exports to-do list information
for a given employee ID to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    UserId = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    User = requests.get(link + "users/{}".format(UserId)).json()
    UserName = User.get("username")
    Task = requests.get(link + "todos", params={"userId": UserId}).json()

    with open("{}.csv".format(UserId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [UserId, UserName, t.get("completed"), t.get("title")]
         ) for t in Task]
