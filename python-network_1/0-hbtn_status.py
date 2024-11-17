#!/usr/bin/python3
"""
This script fetches the status from a given URL using the urllib library.
"""

import urllib.request

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as request:
    print("Body response:")
    data = request.read()
    print(" - type: {}".format(type(data)))
    print(" - content: {}".format(data))
    print(" - utf8 content: {}".format(data.decode("utf-8")))

