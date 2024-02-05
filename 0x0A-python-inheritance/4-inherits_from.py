#!/usr/bin/python3
"""Checks whether the object is an instance of a class 
that has inherited from the specified class or not.
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that has 
    inherited (either directly or indirectly) from the specified class; 
    otherwise, returns False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
