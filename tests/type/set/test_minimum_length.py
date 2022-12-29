import pytest

import valtypes.error.parsing.sized as error
import valtypes.type.set as type


class Set(type.MinimumLength[object]):
    __minimum_length__ = 2


def test_raises_error_if_length_is_less_than_minimum() -> None:
    with pytest.raises(error.MinimumLength) as info:
        Set({1})

    assert info.value == error.MinimumLength(2, 1)


def test_succeeds_if_length_equals_to_minimum() -> None:
    Set({1, 2})


def test_succeeds_if_length_is_greater_than_minimum() -> None:
    Set({1, 2, 3})
