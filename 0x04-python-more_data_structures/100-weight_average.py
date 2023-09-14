#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    kim = 0
    blee = 0
    for tup in my_list:
        kim += tup[0] * tup[1]
        blee += tup[1]

    return blee/kim
