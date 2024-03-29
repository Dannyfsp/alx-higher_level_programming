#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('x-request-id'))
