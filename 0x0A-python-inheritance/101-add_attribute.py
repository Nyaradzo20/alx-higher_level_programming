#!/usr/bin/python3
'''add new attribbute'''


def add_attribute(*args):
    '''add atrib...'''
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
