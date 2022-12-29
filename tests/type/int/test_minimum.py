import pytest

import valtypes.error.parsing.int as error
import valtypes.type.int as type


class Int(type.Minimum):
    __minimum__ = 10


def test_raises_error_if_value_is_less_than_minimum() -> None:
    with pytest.raises(error.Minimum) as info:
        Int(9)

    assert info.value == error.Minimum(10, 9)


def test_succeeds_if_value_equals_to_minimum() -> None:
    Int(10)


def test_succeeds_if_value_is_greater_than_minimum() -> None:
    Int(11)
