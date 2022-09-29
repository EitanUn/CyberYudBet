"""
Author: Eitan Unger
Date: 22/09/22
This file contains the square class inheriting from rectangle
"""
import os
if os.path.exists("rectangle.py"):
    from rectangle import *
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


if __name__ == '__main__':
    test = Square("Red", 15)
    assert test.get_color() == "Red"
    assert test.get_area() == 225
    assert test.get_perimeter() == 60
    assert test.get_side() == 15
