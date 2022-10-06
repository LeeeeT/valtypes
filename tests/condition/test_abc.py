import pytest

from valtypes import decorator
from valtypes.condition import And, Decorated, Is, Not, Or


def test_and_returns_and() -> None:
    assert Is(1) & Is(2) == And(Is(1), Is(2))


def test_and_not_implemented() -> None:
    with pytest.raises(TypeError):
        Is(1) & 2  # type: ignore


def test_or_returns_or() -> None:
    assert Is(1) | Is(2) == Or(Is(1), Is(2))


def test_or_not_implemented() -> None:
    with pytest.raises(TypeError):
        Is(1) | 2  # type: ignore


def test_rrshift_returns_decorated() -> None:
    assert decorator.FromCallable(int) >> Is(1) == Decorated(decorator.FromCallable(int), Is(1))


def test_rrshift_not_implemented() -> None:
    with pytest.raises(TypeError):
        int >> Is(1)  # type: ignore


def test_invert_returns_not() -> None:
    assert ~Is(1) == Not(Is(1))
