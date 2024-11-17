#!/usr/bin/python3
"""
This script displays the value of the 'X-Request-Id' header found in the response.
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as request:
    print(request.getheader("X-Request-Id"))
