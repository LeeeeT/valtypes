import pytest

from valtypes import BaseParsingError, parse


def test_instance() -> None:
    """
    It returns a value itself if it is an instance of the desired type
    """

    assert parse(bytes, b"123") == b"123"


def test_not_instance() -> None:
    """
    It throws an error if a value is not an instance of the desired type
    """

    class Class:
        pass

    with pytest.raises(BaseParsingError):
        parse(Class, 1)
