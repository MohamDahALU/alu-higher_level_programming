#!/usr/bin/python3

import sys
import urllib.request

"""
This script displays the value of the 'X-Request-Id' header found in the response.
"""

with urllib.request.urlopen(sys.argv[1]) as request:
    print(request.getheader("X-Request-Id"))
