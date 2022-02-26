from typing import Generic, TypeVar

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import mapping_to_dict

T = TypeVar("T")

F = TypeVar("F")


def test_simple() -> None:
    assert mapping_to_dict.parse(dict[str, int], {False: "0.0", 1: "1"}, collection) == {"False": 0, "1": 1}


def test_custom_type() -> None:
    class MyDict(dict[T, F], Generic[T, F]):
        pass

    assert isinstance(mapping_to_dict.parse(MyDict[str, int], {False: "0.0", 1: "1"}, collection), MyDict)


def test_error() -> None:
    with pytest.raises(ParsingError):
        mapping_to_dict.parse(dict[int, int], {1: 1.5}, collection)
