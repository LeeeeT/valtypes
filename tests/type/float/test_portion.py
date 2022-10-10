import pytest

import valtypes.error.parsing.type.numeric as error
import valtypes.type.float as type


def test_raises_error_if_value_is_greater_than_1() -> None:
    with pytest.raises(error.Maximum) as info:
        type.Portion(2)

    assert info.value == error.Maximum(1, 2)


def test_raises_error_if_value_is_less_than_0() -> None:
    with pytest.raises(error.Minimum) as info:
        type.Portion(-1)

    assert info.value == error.Minimum(0, -1)


def test_succeeds_if_value_equals_to_1() -> None:
    type.Portion(1)


def test_succeeds_if_value_equals_to_0() -> None:
    type.Portion(0)


def test_succeeds_if_value_is_between_0_and_1() -> None:
    type.Portion(0.5)
