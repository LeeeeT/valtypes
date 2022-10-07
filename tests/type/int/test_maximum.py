import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.int as type


class Int(type.Maximum):
    __maximum__ = 10


def test_greater() -> None:
    """
    It raises an error if the value is greater than the maximum
    """

    with pytest.raises(error.Maximum) as info:
        Int(11)

    assert info.value == error.Maximum(10, 11)


def test_equals() -> None:
    """
    It succeeds if the value equals to the maximum
    """

    Int(10)


def test_less() -> None:
    """
    It succeeds if the value is less than the maximum
    """

    Int(9)
