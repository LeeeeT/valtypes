import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


class Float(type.Maximum):
    __maximum__ = 10


def test_raises_error_if_value_is_greater_than_maximum() -> None:
    with pytest.raises(error.Maximum) as info:
        Float(11)

    assert info.value == error.Maximum(10, 11)


def test_raises_error_if_value_equals_to_maximum() -> None:
    Float(10)


def test_succeeds_if_value_is_less_than_maximum() -> None:
    """
    It succeeds if the value is less than the maximum
    """

    Float(9)
