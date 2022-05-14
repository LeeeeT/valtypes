import pytest

from valtypes import BaseParsingError, parse


def test_supports_index() -> None:
    """
    It converts objects supporting __index__ to float
    """

    class SupportsIndex:
        def __index__(self) -> int:
            return 2

    assert parse(float, SupportsIndex()) == 2.0


def test_supports_float() -> None:
    """
    It converts objects supporting __float__ to float
    """

    class SupportsFloat:
        def __float__(self) -> float:
            return 3.1

    assert parse(float, SupportsFloat()) == 3.1


def test_bytes() -> None:
    """
    It parses bytes representation of float to float
    """

    assert parse(float, b"1.23") == 1.23


def test_bytearray() -> None:
    """
    It parses bytearray representation of float to float
    """

    assert parse(float, bytearray("66.6", "utf-8")) == 66.6


def test_str() -> None:
    """
    It parses str representation of float to float
    """

    assert parse(float, ".4") == 0.4


def test_error() -> None:
    """
    It raises an error if it can't convert the value to float
    """

    with pytest.raises(BaseParsingError):
        parse(float, ".")
