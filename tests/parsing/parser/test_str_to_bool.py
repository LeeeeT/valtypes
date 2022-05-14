import pytest

from valtypes import BaseParsingError, parse


def test() -> None:
    """
    It returns False if the string is falsy and True if the string is truthy (case-insensitive)
    """

    assert parse(bool, "no") is False
    assert parse(bool, "YeS") is True


def test_error() -> None:
    """
    It raises an error if the string doesn't represent a boolean
    """

    with pytest.raises(BaseParsingError):
        parse(bool, "yea")
