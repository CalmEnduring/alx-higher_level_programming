#!/usr/bin/python3
"""a module to convert json to string"""


from json import loads


def from_json_string(my_str):
    """a function that converts json to string"""
    return (loads(my_str))
