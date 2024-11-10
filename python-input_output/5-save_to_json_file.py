#!/usr/bin/python3
"""
This module provides a function to save an object to
a file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.
    """
    jsonData = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(jsonData)
