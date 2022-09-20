#!/usr/bin/python3
"""Creating a locked class"""


class LockedClass:
    """
    A locked class that prevents the user from dynamically creating
    new instance attributes, except if the new instance
    attribute is called 'first_name'
    """
    __slots__ = ["first_name"]
