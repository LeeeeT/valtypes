import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import object_to_union


def test_simple() -> None:
    assert isinstance(object_to_union.parse(int | float | bool, "1.0", collection), int)
    assert object_to_union.parse(int | float | bool, "1.5", collection) == 1.5
    assert object_to_union.parse(int | float | bool, "yes", collection) is True


def test_error() -> None:
    with pytest.raises(ParsingError):
        object_to_union.parse(int | bool, 1.5, collection)
