import pytest

from valtypes.parsing import collection
from valtypes.parsing.parser import floatable_to_float


def test_simple() -> None:
    assert floatable_to_float.parse(float, "1.23", collection) == 1.23
    assert floatable_to_float.parse(float, b"1", collection) == 1.0


def test_custom_type() -> None:
    class MyFloat(float):
        pass

    assert isinstance(floatable_to_float.parse(MyFloat, 2, collection), MyFloat)


def test_error() -> None:
    with pytest.raises(ValueError):
        floatable_to_float.parse(float, "twenty", collection)
