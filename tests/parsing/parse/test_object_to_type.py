import pytest

import valtypes.error.parsing as error
from valtypes import parse


def test_returns_value_if_it_is_instance_of_type() -> None:
    assert parse(int, 1) == 1
    assert parse(bool, True) is True


def test_raises_error_if_value_is_not_instance_of_type() -> None:
    with pytest.raises(error.WrongType) as info:
        parse(int, "1")

    assert info.value == error.WrongType("1", int)

    with pytest.raises(error.WrongType) as info:
        parse(float, 1)

    assert info.value == error.WrongType(1, float)
