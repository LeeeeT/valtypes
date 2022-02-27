from typing import Generic, TypeVar

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_list

T = TypeVar("T")


def test_untyped() -> None:
    assert iterable_to_list.parse(list, [1, "2", b"3"], collection) == [1, "2", b"3"]


def test_typed() -> None:
    assert iterable_to_list.parse(list[int], (1, "2", b"3"), collection) == [1, 2, 3]


def test_custom_type() -> None:
    class MyList(list[T], Generic[T]):
        pass

    assert isinstance(iterable_to_list.parse(MyList[str], range(5), collection), MyList)


def test_error() -> None:
    with pytest.raises(ParsingError):
        iterable_to_list.parse(list[int], (1, "2.5", b"3"), collection)
