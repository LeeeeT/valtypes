import pytest

import valtypes.error.parsing.type.sized as error
import valtypes.type.list as type


class List(type.MaximumLength[object]):
    __maximum_length__ = 2


def test_raises_error_if_length_is_greater_than_maximum() -> None:
    with pytest.raises(error.MaximumLength) as info:
        List([1, 2, 3])

    assert info.value == error.MaximumLength(2, 3)


def test_succeeds_if_length_equals_to_maximum() -> None:
    List([1, 2])


def test_succeeds_if_length_is_less_than_maximum() -> None:
    List([1])
