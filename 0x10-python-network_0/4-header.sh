#!/bin/bash
# A script that takes in a URL as an arg, sends a GET request to the URL, and displays the response body
curl -sH "X-School-User-Id:98" "$1"
