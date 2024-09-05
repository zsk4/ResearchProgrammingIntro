"""
Test if points are in a given bounding box using shapely.

Zachary Katz
zachary_katz@mines.edu
September 2024

Functions
---------
in_box
    Return true if point is in box
"""

import shapely.geometry

class BountingBox:
    """Rectangular bounding box given by its four corners."""

    def __init__(self, box: list[tuple]) -> None:
        """Initialize a bounding box.

        Parameters
        ----------
        box : list[tuple]
            List of four tuples representing the four corners of the box.
        """
        self.box = shapely.geometry.Polygon(box)

    def in_box(self, points: list[tuple]) -> list[bool]:
        """Determine if points are in the bounding box.

        Parameters
        ----------
        points : list[tuple]
            List of tuples representing points to check.

        Returns
        -------
        list[bool]
            List of bools, true if point is in box.
        """
        return self.box.contains(shapely.geometry.Point(points))