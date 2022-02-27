from typing import Generic, TypeVar

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_variable_length_tuple

T = TypeVar("T")


def test_untyped() -> None:
    assert iterable_to_variable_length_tuple.parse(tuple, [1, "2", b"3"], collection) == (1, "2", b"3")


def test_typed() -> None:
    assert iterable_to_variable_length_tuple.parse(tuple[int, ...], (1, "2", b"3"), collection) == (1, 2, 3)


def test_custom_type() -> None:
    class MyTuple(tuple[T, ...], Generic[T]):
        pass

    assert isinstance(iterable_to_variable_length_tuple.parse(MyTuple[str], range(5), collection), MyTuple)


def test_error() -> None:
    with pytest.raises(ParsingError):
        iterable_to_variable_length_tuple.parse(tuple[int, ...], (1, "2.5", b"3"), collection)
