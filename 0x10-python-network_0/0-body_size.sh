#!/bin/bash
# A script that gets the size of the response body using curl
curl -s "$1" | wc -c
