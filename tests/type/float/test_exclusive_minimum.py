import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


class Float(type.ExclusiveMinimum):
    __exclusive_minimum__ = 10


def test_raises_error_if_value_is_less_than_exclusive_minimum() -> None:
    with pytest.raises(error.ExclusiveMinimum) as info:
        Float(9)

    assert info.value == error.ExclusiveMinimum(10, 9)


def test_raises_error_if_value_equals_to_exclusive_minimum() -> None:
    with pytest.raises(error.ExclusiveMinimum) as info:
        Float(10)

    assert info.value == error.ExclusiveMinimum(10, 10)


def test_succeeds_if_value_is_greater_than_exclusive_minimum() -> None:
    Float(11)
