#!/usr/bin/python3

class Square:
    """Class representing a square."""

    def __init__(self, width=0, height=0):
        """Initialize the square with width and height.

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return 4 * self.width

    def __str__(self):
        """Return a string representation of the square."""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=12)  # Using same value for width and height for a square
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
