import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


class Float(type.ExclusiveMaximum):
    __exclusive_maximum__ = 10


def test_greater() -> None:
    """
    It raises an error if the value is greater than the exclusive maximum
    """

    with pytest.raises(error.ExclusiveMaximum) as info:
        Float(11)

    assert info.value == error.ExclusiveMaximum(10, 11)


def test_equals() -> None:
    """
    It raises an error if the value equals to the exclusive maximum
    """

    with pytest.raises(error.ExclusiveMaximum) as info:
        Float(10)

    assert info.value == error.ExclusiveMaximum(10, 10)


def test_less() -> None:
    """
    It succeeds if the value is less than the exclusive maximum
    """

    Float(9)
