import pytest

import valtypes.error.float as error
import valtypes.type.float as type


def test_negative() -> None:
    """
    It raises an error if the value is negative
    """

    with pytest.raises(error.ExclusiveMinimum) as info:
        type.Positive(-1)

    assert info.value == error.ExclusiveMinimum(0, -1)


def test_0() -> None:
    """
    It raises an error if the value equals to 0
    """

    with pytest.raises(error.ExclusiveMinimum) as info:
        type.Positive(0)

    assert info.value == error.ExclusiveMinimum(0, 0)


def test_positive() -> None:
    """
    It succeeds if the value is positive
    """

    type.Positive(1)
