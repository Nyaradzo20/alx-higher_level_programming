#!/usr/bin/python3
"""
This module has one fuction,add and return an integer
"""


def add_integer(a, b):
    """
    add_integer:
    Return sum of a and b, cast as int if float
    raise error if not int or float types
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")

    return int(a) + int(b)