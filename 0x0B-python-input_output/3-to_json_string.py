#!/usr/bin/python3
from json import dumps
"""Serialize

This module demonstrates the converstion of an object(string)
to a JSON representation

"""


def to_json_string(my_obj):
    """a function that converts to json"""
    return (dumps(my_obj))
