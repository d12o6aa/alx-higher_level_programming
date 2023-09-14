#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write_file - reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file
        text: the text of file
    """
    with open(filename, 'w', encoding="utf-8") as myfile:
        myfile.write(text)
