#!/usr/bin/python3
def remove_char_at(str, n):
    """This creates a copy of the string
    without the character at position n"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
