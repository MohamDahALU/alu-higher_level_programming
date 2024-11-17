#!/usr/bin/python3
"""
This is a script that makes a post request with data and
then prints the response.
"""

import sys
import urllib.request


data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")

req = urllib.request.Request(sys.argv[1], data)

with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
    print(body)
