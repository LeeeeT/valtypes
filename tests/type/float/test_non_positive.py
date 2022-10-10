import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


def test_raises_error_if_value_is_positive() -> None:
    with pytest.raises(error.Maximum) as info:
        type.NonPositive(1)

    assert info.value == error.Maximum(0, 1)


def test_succeeds_if_value_equals_to_0() -> None:
    type.NonPositive(0)


def test_succeeds_if_value_is_negative() -> None:
    type.NonPositive(-1)
