from typing import Generic, TypeVar

from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_list

T = TypeVar("T")


def test_untyped() -> None:
    assert iterable_to_list.parse(list, (1, "2", b"3"), collection) == [1, "2", b"3"]


def test_typed() -> None:
    assert iterable_to_list.parse(list[int], (1, "2", b"3"), collection) == [1, 2, 3]


def test_custom_type() -> None:
    class MyList(list[T], Generic[T]):
        pass

    assert isinstance(iterable_to_list.parse(MyList[str], range(5), collection), MyList)
    assert iterable_to_list.parse(MyList[bool], ["yes", "no", 0, 1], collection) == [True, False, False, True]
