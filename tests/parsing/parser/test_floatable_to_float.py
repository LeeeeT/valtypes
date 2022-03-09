import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import floatable_to_float


def test_supports_float() -> None:
    """
    It should accept objects with __float__ method
    """

    class A:
        def __float__(self) -> float:
            return 2.71

    assert floatable_to_float.parse(float, A(), collection) == 2.71


def test_supports_index() -> None:
    """
    It should accept objects with __index__ method
    """

    class A:
        def __index__(self) -> int:
            return 42

    assert floatable_to_float.parse(float, A(), collection) == 42.0


def test_str() -> None:
    """
    It should parse str
    """

    assert floatable_to_float.parse(float, "12", collection) == 12.0


def test_bytes() -> None:
    """
    It should parse bytes
    """

    assert floatable_to_float.parse(float, b"1", collection) == 1.0


def test_bytearray() -> None:
    """
    It should parse bytearray
    """

    assert floatable_to_float.parse(float, bytearray("3.14", "utf-8"), collection) == 3.14


def test_custom_type() -> None:
    """
    It should parse to subclasses of float
    """

    class MyFloat(float):
        pass

    assert isinstance(floatable_to_float.parse(MyFloat, 2, collection), MyFloat)


def test_non_float() -> None:
    """
    It should throw an error if the given value does not represent a float
    """

    with pytest.raises(ParsingError):
        floatable_to_float.parse(float, "", collection)
