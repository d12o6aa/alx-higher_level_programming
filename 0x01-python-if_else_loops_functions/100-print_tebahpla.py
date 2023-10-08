#!/usr/bin/python3

a = 122
while a >= 97:
    if a % 2 == 0:
        print("{}".format(chr(a)), end="")
    else:
        print("{}".format(chr(a - 32)), end="")
    a -= 1
