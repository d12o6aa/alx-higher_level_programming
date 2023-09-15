#!/usr/bin/python3
"""Module for saving to json"""
"""os module"""
import os
"""7-add_item.py module"""

"""6-load_from_json_file.py module"""
"""5-save_to_json_file module"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
list = []
if os.path.exists(file) == False:
    
    add = save_to_json_file(list, file)

else:
    add1 = load_from_json_file(file)
    for x in add1:
        list.append(x)

    data = input().split()
    for x in data:
        list.append(x)


    add = save_to_json_file(list, file)

    add1 = load_from_json_file(file)
