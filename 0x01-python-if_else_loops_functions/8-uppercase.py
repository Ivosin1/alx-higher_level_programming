#!/usr/bin/python3
def uppercase(str):
    """This prints string in uppercase."""
    print("".join(["{:c}".format(ord(c)-32)
          if ord(c) in range(97, 123) else c
          for c in str]))
