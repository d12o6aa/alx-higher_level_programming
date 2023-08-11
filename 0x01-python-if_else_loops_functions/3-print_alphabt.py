#!/usr/bin/python3
x = 97
while x <= 122:
    if chr(x) == 'q':
        x += 1
        continue
    elif chr(x) == 'e':
        x += 1
        continue
    print("{}".format(chr(x)), end="")
    x += 1
