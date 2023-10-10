#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """
    :param obj:
    :param a_class:
    :return: True if the object is an instance of, or if the object
    is an instanceof a class that
    inherited from, the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
