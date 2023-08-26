#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        n = 1
        for i in range(b):
            n = a * n
        if n < 0:
            return n * -1
        else:
            return n
    else:
        n = 1
        for i in range(b * -1):
            n = n / a
        if n < 0:
            return n * -1
        else:
            return n
