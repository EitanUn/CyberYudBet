"""
Author: Eitan Unger
Date: 22/09/22
This file contains the circle class, inheriting from shape
"""
from math import pi
import os
if os.path.exists("shape.py"):
    from shape import *
else:
    raise AssertionError("Missing file: Shape.py")



class Circle(Shape):
    """
    Circle class, inheriting from shape
    """
    def __init__(self, color="blue", radius=1):
        """
        circle constructor
        :param color: circle's color
        :param radius: circle's radius
        """
        super().__init__(color, pi*(radius**2), 2*pi*radius)
        self.__radius = radius

    def get_radius(self):
        return self.__radius


if __name__ == '__main__':
    test = Circle("Red", 15)
    assert test.get_color() == "Red"
    assert test.get_area() == pi*225
    assert test.get_perimeter() == 30*pi
    assert test.get_radius() == 15
