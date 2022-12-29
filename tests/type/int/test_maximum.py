import pytest

import valtypes.error.parsing.int as error
import valtypes.type.int as type


class Int(type.Maximum):
    __maximum__ = 10


def test_raises_error_if_value_is_greater_than_maximum() -> None:
    with pytest.raises(error.Maximum) as info:
        Int(11)

    assert info.value == error.Maximum(10, 11)


def test_succeeds_if_value_equals_to_maximum() -> None:
    Int(10)


def test_succeeds_if_value_is_less_than_maximum() -> None:
    Int(9)
