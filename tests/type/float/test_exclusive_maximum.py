import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


class Float(type.ExclusiveMaximum):
    __exclusive_maximum__ = 10


def test_raises_error_if_value_is_greater_than_exclusive_maximum() -> None:
    with pytest.raises(error.ExclusiveMaximum) as info:
        Float(11)

    assert info.value == error.ExclusiveMaximum(10, 11)


def test_raises_error_if_value_equals_to_exclusive_maximum() -> None:
    with pytest.raises(error.ExclusiveMaximum) as info:
        Float(10)

    assert info.value == error.ExclusiveMaximum(10, 10)


def test_succeeds_if_value_is_less_than_exclusive_maximum() -> None:
    Float(9)
