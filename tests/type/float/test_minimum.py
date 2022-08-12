import pytest

import valtypes.error.float as error
import valtypes.type.float as type


class Float(type.Minimum):
    __minimum__ = 10


def test_less() -> None:
    """
    It raises an error if the value is less than the minimum
    """

    with pytest.raises(error.Minimum) as info:
        Float(9)

    assert info.value == error.Minimum(10, 9)


def test_equals() -> None:
    """
    It succeeds if the value equals to the minimum
    """

    Float(10)


def test_greater() -> None:
    """
    It succeeds if the value is greater than the minimum
    """

    Float(11)
