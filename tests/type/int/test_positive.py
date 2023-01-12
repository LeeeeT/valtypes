import pytest

import valtypes.error.parsing.int as error
import valtypes.type.int as type


def test_raises_error_if_value_is_negative() -> None:
    with pytest.raises(error.Minimum) as info:
        type.Positive(-1)

    assert info.value == error.Minimum(1, -1)


def test_raises_error_if_value_equals_to_0() -> None:
    with pytest.raises(error.Minimum) as info:
        type.Positive(0)

    assert info.value == error.Minimum(1, 0)


def test_succeeds_if_value_is_positive() -> None:
    type.Positive(1)
