import math

import pytest

from learning_classes.shapes import Circle, Rectangle, Shape, Square, total_area


def test_cannot_instantiate_abstract_shape():
    with pytest.raises(TypeError):
        Shape("nothing")


def test_rectangle():
    r = Rectangle(2, 3)
    assert r.area() == 6
    assert r.perimeter() == 10


def test_square_is_a_rectangle():
    s = Square(4)
    assert isinstance(s, Rectangle)
    assert isinstance(s, Shape)
    assert s.area() == 16
    assert s.name == "Square"


def test_circle():
    c = Circle(1)
    assert c.area() == pytest.approx(math.pi)
    assert c.perimeter() == pytest.approx(2 * math.pi)


def test_describe():
    assert Rectangle(2, 3).describe() == "Rectangle: area=6.00, perimeter=10.00"


def test_total_area_polymorphism():
    assert total_area([Rectangle(2, 3), Square(2)]) == 10
