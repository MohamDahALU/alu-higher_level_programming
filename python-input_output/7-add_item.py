#!/usr/bin/python3
"""
This module provides a script to add command line 
arguments to a list stored in a JSON file.
"""

import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


arr = load_from_json_file("add_item.json")

arr += sys.argv[1:]

save_to_json_file(arr, "add_item.json")
