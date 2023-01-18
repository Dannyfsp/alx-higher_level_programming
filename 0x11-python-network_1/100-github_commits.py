#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.agrv[1]
    owner_name = sys,argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repository_name)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
