import pytest

import valtypes.error.float as error
import valtypes.type.float as type


def test_greater_than_1() -> None:
    """
    It raises an error if the value is greater than 1
    """

    with pytest.raises(error.Maximum) as info:
        type.Portion(2)

    assert info.value == error.Maximum(1, 2)


def test_less_than_0() -> None:
    """
    It raises an error if the value is less than 0
    """

    with pytest.raises(error.Minimum) as info:
        type.Portion(-1)

    assert info.value == error.Minimum(0, -1)


def test_1() -> None:
    """
    It succeeds if the value equals to 1
    """

    type.Portion(1)


def test_0() -> None:
    """
    It succeeds if the value equals to 0
    """

    type.Portion(0)


def test_between_0_and_1() -> None:
    """
    It succeeds if the value is between 0 and 1
    """

    type.Portion(0.5)
