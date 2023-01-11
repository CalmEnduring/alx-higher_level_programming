#!/usr/bin/python3
from json import dumps
"""a module to return the JSON representation of an object(string)"""


def to_json_string(my_obj):
    """a function that converts to json"""
    return (dumps(my_obj))
