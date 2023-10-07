#!/usr/bin/python3
"""
=============================
Module with the method MyList
=============================
"""


class MyList(list):
    """Mylist class - inherits from list"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))

