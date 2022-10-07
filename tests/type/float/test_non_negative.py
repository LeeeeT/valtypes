import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


def test_negative() -> None:
    """
    It raises an error if the value is negative
    """

    with pytest.raises(error.Minimum) as info:
        type.NonNegative(-1)

    assert info.value == error.Minimum(0, -1)


def test_0() -> None:
    """
    It succeeds if the value equals to 0
    """

    type.NonNegative(0)


def test_positive() -> None:
    """
    It succeeds if the value is positive
    """

    type.NonNegative(1)
