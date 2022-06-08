#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
       In Python, Set is an unordered collection of
       data type that is iterable, mutable and has no duplicate elements.
    '''
    my_list = set(my_list)
    return sum(my_list)
