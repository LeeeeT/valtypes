import pytest

from valtypes import BaseParsingError, parse


def test_integer_float() -> None:
    """
    It converts an integer float to int
    """

    assert parse(int, 69.0) == 69
    assert isinstance(parse(int, 69.0), int)


def test_non_integer() -> None:
    """
    It throws an error if a float is not an integer
    """

    with pytest.raises(BaseParsingError):
        parse(int, 3.14)
