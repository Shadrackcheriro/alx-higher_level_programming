#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k in list(a_dictionary.keys()):
        if a_dictionary.get(k) == value:
            del a_dictionary[k]
    return a_dictionary
