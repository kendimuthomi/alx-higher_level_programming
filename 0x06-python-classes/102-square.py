#!/usr/bin/python3
"""create a class"""


class Square:
    """initialize an instance of square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
    
    def __eq__(self, other):
        """check if equal to another square"""
        return(self.area() == other.area())

    def __let__(self, other):
        """check if less than other square"""
        return(self.area() < other.area())

    def __leeq__(self, other):
        """check if less than or equal to other square"""
        return(self.area() <= other.area())

    def __neq__(self, other):
        """check if not equal to another suqare"""
        return(self.area() != other.area())

    def __grt__(self, other):
        """check if greater than another square"""
        return(self.area() > other.area())

    def __greq__(self, other):
        """check if greater than or equal to another square"""
        return(self.area() >= other.area())
