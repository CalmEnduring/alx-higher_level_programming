#!/usr/bin/python3
"""a module to check if instance/object is part of
   a class that inherited from specified class
   """


def is_kind_of_class(obj, a_class):
    """functions checks if instance/object is part of
       a class that inherited from specified class
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
