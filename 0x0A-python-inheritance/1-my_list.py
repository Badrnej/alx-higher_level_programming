#!/usr/bin/python3
"""This module is derived from the list class."""


class MyList(list):
    """A class that is derived from the list class."""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
