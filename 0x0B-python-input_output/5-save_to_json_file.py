#!/usr/bin/python3
"""

This module demonstrates writing an object to a file
using a JSON representation.

"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """

    The function that converts the object to JSON representation
    and writes it to a file

    """
    with open(filename, "w", encoding="utf-8") as json_file:
        jsonrep = dumps(my_obj)
        return json_file.write(jsonrep)
