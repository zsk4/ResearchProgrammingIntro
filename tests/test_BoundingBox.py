import src.BoundingPolygon as BoundingPolygon
import pytest

def test_inPolygon():
    """Test cases for inPolygon as an axes-aligned box."""
    # Multiple points
    box = BoundingPolygon.BoundingPolygon([(0, 0), (0, 1), (1, 1), (1, 0),(0, 0)])
    points = [(0.5, 0.5), (2, 2),(-4,-4)]
    assert box.inPolygon(points) == [True, False, False]

    # Empty list
    box = BoundingPolygon.BoundingPolygon([(0, 0), (0, 1), (1, 1), (1, 0),(0, 0)])
    points = []
    assert box.inPolygon(points) == []

    # On Edge, Single Point
    box = BoundingPolygon.BoundingPolygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
    points = [(0.5, 0)]
    assert box.inPolygon(points) == [True]
