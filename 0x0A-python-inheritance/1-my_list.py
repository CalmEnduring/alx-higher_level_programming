#!/usr/bin/python3
"""a module that prints an ascending order list"""


class MyList(list):
    """"a class that is a base class"""

    def print_sorted(self):
        """
        prints a list in ascending order

        it sorts the lists and prints it
        """

        if issubclass(MyList, list):
            print(sorted(self))
