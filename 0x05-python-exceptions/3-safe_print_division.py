#!/usr/bin/python3

def safe_print_division(a, b):
    v = None
    try:
        v = a / b
        # print("{} / {}".format(a, b))
        return v
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(v))
