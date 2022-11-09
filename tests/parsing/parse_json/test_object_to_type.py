import pytest

import valtypes.error.parsing as error
from valtypes import parse_json


def test_returns_value_if_it_is_instance_of_type() -> None:
    assert parse_json(int, 1) == 1
    assert parse_json(bool, True) is True


def test_raises_error_if_value_is_not_instance_of_type() -> None:
    with pytest.raises(error.WrongType) as info:
        parse_json(int, "1")

    assert info.value == error.WrongType(int, "1")

    with pytest.raises(error.WrongType) as info:
        parse_json(float, 1)

    assert info.value == error.WrongType(float, 1)
