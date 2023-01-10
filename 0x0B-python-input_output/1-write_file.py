#!/usr/bin/python3
"""a module to write text to a file and return number of characters"""


def write_file(filename="", text=""):
    """a function that writes to a txt file 
       and returns number of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
