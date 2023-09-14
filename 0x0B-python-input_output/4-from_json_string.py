#!/usr/bin/python3
"""
    json module
"""
import json
"""3-from_json_string module"""


def from_json_string(my_str):
    """
    from_json_string -  returns an object (Python data structure)
    represented by a JSON string.
    :param my_str: dictionary
    :return: JSON representation
    """

    return json.loads(my_str)
