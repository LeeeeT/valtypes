import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.int as type


def test_negative() -> None:
    """
    It raises an error if the value is negative
    """

    with pytest.raises(error.Minimum) as info:
        type.Positive(-1)

    assert info.value == error.Minimum(1, -1)


def test_0() -> None:
    """
    It raises an error if the value equals to 0
    """

    with pytest.raises(error.Minimum) as info:
        type.Positive(0)

    assert info.value == error.Minimum(1, 0)


def test_positive() -> None:
    """
    It succeeds if the value is positive
    """

    type.Positive(1)
