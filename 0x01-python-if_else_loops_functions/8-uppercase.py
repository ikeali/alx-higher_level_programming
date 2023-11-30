#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = i
        if ord(j) >= 97 and ord(j) <= 122:
            j = chr(ord(i) - 32)
        print("{}".format(j), end='')
    print()
