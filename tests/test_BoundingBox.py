import src.BoundingBox as BoundingBox
import pytest

def test_inBox():
    """Test cases for inBox."""
    # Single point in box
    box = BoundingBox.BoundingBox([(0, 0), (0, 1), (1, 1), (1, 0)])
    points = [(0.5, 0.5)]
    assert box.inBox(points) == [True]

    # Single point outside box
    box = BoundingBox.BoundingBox([(0, 0), (0, 1), (2, 1), (2, 0)])
    points = [(4, 2)]
    assert box.inBox(points) == [False]

    # Multiple points
    box = BoundingBox.BoundingBox([(0, 0), (0, 1), (1, 1), (1, 0)])
    points = [(0.5, 0.5), (2, 2)]
    assert box.inBox(points) == [True, False]

    # Empty list
    box = BoundingBox.BoundingBox([(0, 0), (0, 1), (1, 1), (1, 0)])
    points = []
    assert box.inBox(points) == []

    # On Edge
    box = BoundingBox.BoundingBox([(0, 0), (0, 1), (1, 1), (1, 0)])
    points = [(0.5, 0)]
    assert box.inBox(points) == [True]
