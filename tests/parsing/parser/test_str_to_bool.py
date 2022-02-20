import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import str_to_bool


def test_simple() -> None:
    assert str_to_bool.parse(bool, "0", collection) is False
    assert str_to_bool.parse(bool, "YeS", collection) is True


def test_error() -> None:
    with pytest.raises(ParsingError):
        str_to_bool.parse(bool, "yea", collection)
