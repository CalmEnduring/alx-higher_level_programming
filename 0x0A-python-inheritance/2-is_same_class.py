#!/usr/bin/python3
"""a module to check whether an object belongs to a class"""


def is_same_class(obj, a_class):
    """a function that checks whether an object belongs to a class"""
    if type(obj) == a_class:
        return True

    return False
