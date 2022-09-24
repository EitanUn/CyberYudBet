"""
Author: Eitan Unger
Date: 22/09/22
This file contains the shape container class, which is used to generate, hold and make some calculations on shapes
(must be a circle, a rectangle or a square
"""

from random import *
from functools import reduce
import os
if os.path.exists("circle.py"):
    from shape import *
else:
    raise AssertionError("Missing file: circle.py")

if os.path.exists("square.py.py"):
    from shape import *
else:
    raise AssertionError("Missing file: square.py")

COLORS = ["Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Magenta", "Purple", "White", "Black", "Gray", "Pink",
          "Brown", "Lime", "Indigo", "Violet"]
RAD_MIN = 1
RAD_MAX = 10
SIDE_MIN = 1
SIDE_MAX = 20
COLOR_MIN = 0


class Container:
    """
    shape container class
    """
    def __init__(self):
        """
        create container object and a list-type attribute for holding shapes
        """
        self.__shape_container = []

    def generate(self, num):
        """
        generate a number of different shapes randomly
        :param num: number of shapes to generate
        :return: None
        """
        for i in range(num):
            rand = randint(1, 3)  # choose shape type
            if rand == 1:
                shape = Circle(COLORS[randint(COLOR_MIN, len(COLORS)-1)], randint(RAD_MIN, RAD_MAX))
            elif rand == 2:
                shape = Rectangle(COLORS[randint(COLOR_MIN, len(COLORS)-1)], randint(SIDE_MIN, SIDE_MAX),
                                  randint(SIDE_MIN, SIDE_MAX))
            else:
                shape = Square(COLORS[randint(COLOR_MIN, len(COLORS)-1)], randint(SIDE_MIN, SIDE_MAX))
            self.__shape_container.append(shape)  # add shape to the container

    def sum_areas(self):
        """
        function for summing areas of all shapes in the container
        :return: sum of areas
        """
        return reduce(lambda a, b: a+b, [x.get_area() for x in self.__shape_container])

    def sum_perimeters(self):
        """
        function for summing perimeters of all shapes in the container
        :return: sum of perimeters
        """
        return reduce(lambda a, b: a+b, [x.get_perimeter() for x in self.__shape_container])

    def count_colors(self):
        """
        function for counting appearances of colors in the container
        :return: dictionary of the form color: appearance
        """
        color_dict = {i: 0 for i in COLORS}  # make dictionary
        for shape in self.__shape_container:
            color_dict[shape.get_color()] += 1  # count appearances for each color
        return color_dict


my_container = Container()
my_container.generate(100)
print("total area:", my_container.sum_areas())
print("total perimeter:", my_container.sum_perimeters())
print("colors:", my_container.count_colors())
