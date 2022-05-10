import pytest

from valtypes import BaseParsingError, parse


def test_parse_items() -> None:
    """
    It parses items of iterable to desired types
    """

    assert parse(tuple[bytes, int, str], (1, "2", b"3")) == (b"1", 2, "3")  # type: ignore


def test_wrong_value() -> None:
    """
    It throws an error if some item can't be parsed to desired type
    """

    with pytest.raises(BaseParsingError):
        parse(tuple[float, int], (1, "2.5"))  # type: ignore


def test_not_enough_items() -> None:
    """
    It throws an error if there are not enough items in iterable
    """

    with pytest.raises(BaseParsingError):
        parse(tuple[float, int], (1,))  # type: ignore
