#!/usr/bin/python3
"""
1-write_file module
"""


def append_write(filename="", text=""):
    """
    append_write -  Appends a string at the end of a text file
    (UTF8) and returns the number of characters added:
        filename: name of the file
        text: the text of file
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        myfile.write(text)

    return len(text)
