"""
Author: Eitan Unger
Date: 22/09/22
This file contains the shape class, base for circle, square and rectangle, and some set/get functions
"""


class Shape:
    """
    simple shape class
    """

    def __init__(self, color="blue", area=1, perimeter=1):
        """
        shape constructor function
        :param color: color of the shape
        :param area: area of the shape
        :param perimeter: perimeter of the shape
        """
        self.__area = area
        self.__perimeter = perimeter
        self.__color = color

    def set_color(self, color):
        """
        set function for color attribute
        :param color: color to set to
        """
        self.__color = color

    def set_area(self, area):
        """
        set function for area attribute
        :param area: area to set to
        """
        self.__area = area

    def set_perimeter(self, perimeter):
        """
        set function for perimeter attribute
        :param perimeter: perimeter to set to
        """
        self.__perimeter = perimeter

    def get_color(self):
        """
        get function for color attribute
        :return: the shape's color
        """
        return self.__color

    def get_area(self):
        """
        get function for area attribute
        :return: the shape's area
        """
        return self.__area

    def get_perimeter(self):
        """
        get function for perimeter attribute
        :return: the shape's perimeter
        """
        return self.__perimeter
