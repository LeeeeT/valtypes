import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import float_to_int


def test_integer_float() -> None:
    """
    It should parse an integer float to int
    """

    assert float_to_int.parse(int, 69.0, collection) == 69
    assert isinstance(float_to_int.parse(int, 69.0, collection), int)


def test_custom_type() -> None:
    """
    It should parse to subclasses of int
    """

    class MyInt(int):
        pass

    assert isinstance(float_to_int.parse(MyInt, 1.0, collection), MyInt)


def test_non_integer() -> None:
    """
    It should throw an error if the given float is not an integer
    """

    with pytest.raises(ParsingError):
        float_to_int.parse(int, 3.14, collection)
