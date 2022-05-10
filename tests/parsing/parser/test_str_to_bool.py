import pytest

from valtypes import BaseParsingError, parse


def test() -> None:
    """
    It returns False if a string is falsy and True if a string is truthy (case-insensitive)
    """

    assert parse(bool, "no") is False
    assert parse(bool, "YeS") is True


def test_error() -> None:
    """
    It throws an error if a string does not represent a boolean
    """

    with pytest.raises(BaseParsingError):
        parse(bool, "yea")
