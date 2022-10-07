import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


class Float(type.ExclusiveMinimum):
    __exclusive_minimum__ = 10


def test_less() -> None:
    """
    It raises an error if the value is less than the exclusive minimum
    """

    with pytest.raises(error.ExclusiveMinimum) as info:
        Float(9)

    assert info.value == error.ExclusiveMinimum(10, 9)


def test_equals() -> None:
    """
    It raises an error if the value equals to the exclusive minimum
    """

    with pytest.raises(error.ExclusiveMinimum) as info:
        Float(10)

    assert info.value == error.ExclusiveMinimum(10, 10)


def test_greater() -> None:
    """
    It succeeds if the value is greater than the exclusive minimum
    """

    Float(11)
