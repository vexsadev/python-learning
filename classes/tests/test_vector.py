import dataclasses

import pytest

from learning_classes.vector import Vector


def test_generated_init_repr_eq():
    v = Vector(1, 2)
    assert repr(v) == "Vector(x=1, y=2)"
    assert v == Vector(1, 2)
    assert v != Vector(2, 1)


def test_frozen():
    with pytest.raises(dataclasses.FrozenInstanceError):
        Vector(1, 2).x = 5


def test_frozen_is_hashable():
    assert len({Vector(1, 2), Vector(1, 2)}) == 1


def test_operators():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
    assert Vector(3, 4) - Vector(1, 1) == Vector(2, 3)
    assert Vector(1, 2) * 3 == Vector(3, 6)
    assert 3 * Vector(1, 2) == Vector(3, 6)
    assert abs(Vector(3, 4)) == 5
