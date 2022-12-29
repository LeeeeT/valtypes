import pytest

import valtypes.error.parsing.float as error
import valtypes.type.float as type


def test_raises_error_if_value_is_positive() -> None:
    with pytest.raises(error.ExclusiveMaximum) as info:
        type.Negative(1.0)

    assert info.value == error.ExclusiveMaximum(0.0, 1.0)


def test_raises_error_if_value_equals_to_0() -> None:
    with pytest.raises(error.ExclusiveMaximum) as info:
        type.Negative(0.0)

    assert info.value == error.ExclusiveMaximum(0.0, 0.0)


def test_succeeds_if_value_is_negative() -> None:
    type.Negative(-1.0)
