#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''using map to iterate'''
    newList = list(map(lambda a: replace if a == search else a, my_list))
    return newList
