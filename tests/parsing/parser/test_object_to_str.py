import pytest

from valtypes import BaseParsingError, parse


def test() -> None:
    """
    It calls __str__ to convert object to str
    """

    class Class:
        def __str__(self) -> str:
            return "ah"

    assert parse(str, Class()) == "ah"


def test_error() -> None:
    """
    It throws an error if __str__ throws an error
    """

    class Class:
        def __str__(self) -> str:
            raise Exception

    with pytest.raises(BaseParsingError):
        parse(str, Class())
