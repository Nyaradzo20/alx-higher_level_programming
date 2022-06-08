#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b_dict = max(a_dictionary, key=a_dictionary.get)
        return b_dict
    else:
        return None
