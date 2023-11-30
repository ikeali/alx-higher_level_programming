#!/usr/bin/python3
def remove_char_at(str, n):
    bat = ""
    i = 0
    for x in str:
        if i != n:
            bat += x
        i += 1
    return bat
