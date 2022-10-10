import pytest

import valtypes.error.parsing as error
from valtypes.parsing.parser import ObjectToType


def test_returns_value_if_its_type_is_correct() -> None:
    assert ObjectToType(int).parse(2) == 2


def test_raises_error_if_value_type_is_wrong() -> None:
    with pytest.raises(error.WrongType) as info:
        ObjectToType(int).parse("2")

    assert info.value == error.WrongType("2", int)


def test_eq_returns_true_if_types_are_equal() -> None:
    assert ObjectToType(int) == ObjectToType(int)


def test_eq_returns_false_if_types_are_different() -> None:
    assert ObjectToType(str) != ObjectToType(int)


def test_eq_returns_not_implemented_if_got_not_object_to_type() -> None:
    assert ObjectToType(int) != ...
