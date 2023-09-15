#!/usr/bin/python3

"""
    json module
"""
import json
"""6-load_from_json_file.py module"""


def load_from_json_file(filename):
    """
    load_from_json_file - function that creates an Object from a “JSON file”.
    :param
        filename: the name of file
        return: Object from a “JSON file”
    """

    with open(filename, 'r') as f:
        data = json.load(f)

    return data
