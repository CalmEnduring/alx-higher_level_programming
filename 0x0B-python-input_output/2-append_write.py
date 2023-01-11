#!/usr/bin/python3
"""a module to append a file"""


def append_write(filename="", text=""):
    """a function that appends a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
