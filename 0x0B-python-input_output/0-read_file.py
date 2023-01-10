#!/usr/bin/python3
"""a module to read a text file and prints it"""


def read_file(filename=""):
    """a function that reads a file and prints it"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
