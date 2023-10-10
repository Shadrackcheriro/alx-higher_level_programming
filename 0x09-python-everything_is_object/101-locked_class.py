#!/usr/bin/python3
"""

This is a module that containts a clas that avoids
dynamically created attributes

"""


class LockedClass:
    """This is a module that containts a clas that avoids
dynamically created attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
