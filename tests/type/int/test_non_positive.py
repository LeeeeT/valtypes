import pytest

import valtypes.error.int as error
import valtypes.type.int as type


def test_positive() -> None:
    """
    It raises an error if the value is positive
    """

    with pytest.raises(error.Maximum) as info:
        type.NonPositive(1)

    assert info.value == error.Maximum(0, 1)


def test_0() -> None:
    """
    It succeeds if the value equals to 0
    """

    type.NonPositive(0)


def test_negative() -> None:
    """
    It succeeds if the value is negative
    """

    type.NonPositive(-1)
