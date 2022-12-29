import pytest

import valtypes.error.parsing.int as error
import valtypes.type.int as type


def test_raises_error_if_value_is_negative() -> None:
    with pytest.raises(error.Minimum) as info:
        type.NonNegative(-1)

    assert info.value == error.Minimum(0, -1)


def test_succeeds_if_value_equals_to_0() -> None:
    type.NonNegative(0)


def test_succeeds_if_value_is_positive() -> None:
    type.NonNegative(1)
