from typing import Generic, TypeVar

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_fixed_length_tuple

T = TypeVar("T")

F = TypeVar("F")


def test_simple() -> None:
    assert iterable_to_fixed_length_tuple.parse(tuple[bytes, int, str], (1, "2", b"3"), collection) == (b"1", 2, "3")


def test_custom_type() -> None:
    class MyTuple(tuple[T, float, F], Generic[T, F]):
        pass

    assert isinstance(iterable_to_fixed_length_tuple.parse(MyTuple[bool, int], range(3), collection), MyTuple)


def test_error() -> None:
    with pytest.raises(ParsingError):
        iterable_to_fixed_length_tuple.parse(tuple[float, int], (1, "2.5"), collection)

    with pytest.raises(ParsingError):
        iterable_to_fixed_length_tuple.parse(tuple[float, int], (1,), collection)
