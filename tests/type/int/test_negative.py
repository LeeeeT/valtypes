import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.int as type


def test_raises_error_if_value_is_positive() -> None:
    with pytest.raises(error.Maximum) as info:
        type.Negative(1)

    assert info.value == error.Maximum(-1, 1)


def test_raises_error_if_value_equals_to_0() -> None:
    with pytest.raises(error.Maximum) as info:
        type.Negative(0)

    assert info.value == error.Maximum(-1, 0)


def test_succeeds_if_value_is_negative() -> None:
    type.Negative(-1)
