#!/usr/bin/python3
"""a module to check subclass inheritance"""


def inherits_from(obj, a_class):
    """a function that checks if an object is an instance
       of a class that inherits directly or indirectly from
       the specified class
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True
    else:
        return False
