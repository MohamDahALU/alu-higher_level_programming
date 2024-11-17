#!/usr/bin/python3

# This script takes a URL as a command-line argument, sends a request to the URL,
# and displays the value of the 'X-Request-Id' header found in the response.


import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as request:
    print(request.getheader("X-Request-Id"))
