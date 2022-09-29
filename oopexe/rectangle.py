"""
Author: Eitan Unger
Date: 22/09/22
This file contains the rectangle class, inheriting from shape and base for square
"""
import os
if os.path.exists("shape.py"):
    from shape import *
else:
    raise AssertionError("Missing file: Shape.py")


class Rectangle(Shape):
    """
    Rectangle class, inheriting from shape
    """
    def __init__(self, color="blue", side1=1, side2=1):
        """
        Rectangle constructor
        :param color: rectangle's color
        :param side1: one of the sides
        :param side2: the other side of the rectangle
        """
        super().__init__(color, side1 * side2, 2*(side2+side1))
        self.__side1 = side1
        self.__side2 = side2

    def get_side(self, num=1):
        """
        get function for both side fields
        :param num: which side to get, must be 1 or 2, otherwise return 0
        :return: side length or 0 if not 1 or 2
        """
        if num == 1:
            return self.__side1
        elif num == 2:
            return self.__side2
        else:
            return 0

    def set_side1(self, side):
        """
        set func for side 1, updates area and perimeter
        :param side: value to set to
        """
        self.__side1 = side
        self.set_perimeter(2*(self.get_side(1)+self.get_side(2)))
        self.set_area(self.get_side(1)*self.get_side(2))

    def set_side2(self, side):
        """
        set func for side 2, updates area and perimeter
        :param side: value to set to
        """
        self.__side2 = side
        self.set_perimeter(2*(self.get_side(1)+self.get_side(2)))
        self.set_area(self.get_side(1)*self.get_side(2))

    def combine_shapes(self, shape):
        """
        function for combining 2 rectangle/square shapes if they can share a side, otherwise return None
        :param shape: other shape to connect to self
        :return: new, connected shape or None if they can't connect
        """
        if isinstance(shape, Rectangle):  # make sure the other shape is a rectangle/square
            for i in range(1, 3):
                for j in range(1, 3):
                    if self.get_side(i) == shape.get_side(j):  # check if the 2 shapes share a side
                        return Rectangle(side1=self.get_side(i), side2=(self.get_side(3-i) + shape.get_side(3-j)))
        return None


if __name__ == '__main__':
    test = Rectangle("Red", 15, 5)
    assert test.get_color() == "Red"
    assert test.get_area() == 75
    assert test.get_perimeter() == 40
    assert test.get_side(1) == 15
    assert test.get_side(2) == 5
    test2 = Rectangle("Red", 14, 5)
    assert test.combine_shapes(test2).get_perimeter() == "68"
