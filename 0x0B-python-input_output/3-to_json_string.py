#!/usr/bin/python3
"""
    json module
"""

import json
"""3-to_json_string module"""


def to_json_string(my_obj):
    """
    to_json_string - returns the JSON representation
    of an object (string).
    :param my_obj: dictionary
    :return: JSON representation
    """

    return json.dumps(my_obj, sort_keys=True)
