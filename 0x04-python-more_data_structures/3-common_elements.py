#!/usr/bin/python3
def common_elements(set_1, set_2):
    return list(set(set_1) & set(set_2))
'''
def common_elements(set_1, set_2):
 a = set(set_1)
    b = set(set_2)
    if ( a & b):
        return (a & b)
    else:
        return (None)
'''
