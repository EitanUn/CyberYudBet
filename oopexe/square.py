"""
Author: Eitan Unger
Date: 22/09/22
This file contains the square class inheriting from rectangle
"""
import os
if os.path.exists("rectangle.py"):
    from shape import *
else:
    raise AssertionError("Missing file: rectangle.py")


class Square(Rectangle):
    """
    Square class, inheriting from rectangle
    """
    def __init__(self, color="blue", side=1):
        """
        Square constructor
        :param color: square's color
        :param side: square's side length
        """
        super().__init__(color, side, side)
