import pytest

import valtypes.error.parsing.float as error
import valtypes.type.float as type


class Float(type.Minimum):
    __minimum__ = 10.0


def test_raises_error_if_value_is_less_than_minimum() -> None:
    with pytest.raises(error.Minimum) as info:
        Float(9.0)

    assert info.value == error.Minimum(10.0, 9.0)


def test_succeeds_if_value_equals_to_minimum() -> None:
    Float(10.0)


def test_succeeds_if_value_is_greater_than_minimum() -> None:
    Float(11.0)
