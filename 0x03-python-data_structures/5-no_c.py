#!/usr/bin/python3
def no_c(my_string):
    cC = ["c", "C"]
    return "".join(filter(lambda x: x not in cC, my_string))
