#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file
    """
    with open(filename, encoding="utf-8") as myfile:

        print(myfile.read())
