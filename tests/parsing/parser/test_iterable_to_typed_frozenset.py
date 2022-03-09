from typing import Generic, TypeVar

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_typed_frozenset

T = TypeVar("T")


def test_simple() -> None:
    assert iterable_to_typed_frozenset.parse(frozenset[int], (1, "2", b"3"), collection) == {1, 2, 3}


def test_custom_type() -> None:
    class MyFrozenset(frozenset[T], Generic[T]):
        pass

    assert isinstance(iterable_to_typed_frozenset.parse(MyFrozenset[str], range(5), collection), MyFrozenset)


def test_error() -> None:
    with pytest.raises(ParsingError):
        iterable_to_typed_frozenset.parse(frozenset[int], (1, "2.5", b"3"), collection)
