import pytest

import valtypes.error.float as error
import valtypes.type.float as type


def test_positive() -> None:
    """
    It raises an error if the value is positive
    """

    with pytest.raises(error.ExclusiveMaximum) as info:
        type.Negative(1)

    assert info.value == error.ExclusiveMaximum(0, 1)


def test_0() -> None:
    """
    It raises an error if the value equals to 0
    """

    with pytest.raises(error.ExclusiveMaximum) as info:
        type.Negative(0)

    assert info.value == error.ExclusiveMaximum(0, 0)


def test_negative() -> None:
    """
    It succeeds if the value is negative
    """

    type.Negative(-1)
