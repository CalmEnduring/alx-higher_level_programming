#!/usr/bin/python3
"""

This module demonstrates creating an object from a JSON file.

"""


from json import loads


def load_from_json_file(filename):
    """This function creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as file:
        return loads(file.read())
