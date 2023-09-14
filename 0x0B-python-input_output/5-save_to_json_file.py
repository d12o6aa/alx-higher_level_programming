#!/usr/bin/python3

"""
    json module
"""
import json
"""5-save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file -  function that writes an Object
    to a text file, using a JSON representation.
    :param
        my_obj: dictionary
        filename: the name of file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
