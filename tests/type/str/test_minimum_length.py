import pytest

import valtypes.error.parsing.type.sized as error
import valtypes.type.str as type


class Str(type.MinimumLength):
    __minimum_length__ = 2


def test_raises_error_if_length_is_less_than_minimum() -> None:
    with pytest.raises(error.MinimumLength) as info:
        Str("a")

    assert info.value == error.MinimumLength(2, 1)


def test_succeeds_if_length_equals_to_minimum() -> None:
    Str("ab")


def test_succeeds_if_length_is_greater_than_minimum() -> None:
    Str("abc")
