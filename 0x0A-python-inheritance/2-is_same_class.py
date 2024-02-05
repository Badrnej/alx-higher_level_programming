#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return True if the object is an instance of the class; 
    otherwise, return False
    """
    return (type(obj) == a_class)
