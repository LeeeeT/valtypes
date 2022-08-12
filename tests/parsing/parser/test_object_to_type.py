import pytest

import valtypes.error.parsing as parsing_error
from valtypes.parsing.parser import ObjectToType


def test_passes_when_correct_type() -> None:
    assert ObjectToType(int).parse(2) == 2


def test_raises_when_wrong_type() -> None:
    with pytest.raises(parsing_error.WrongType) as info:
        ObjectToType(int).parse("2")

    assert info.value == parsing_error.WrongType("2", int)


def test_eq_same_types() -> None:
    assert ObjectToType(int) == ObjectToType(int)


def test_eq_different_types() -> None:
    assert ObjectToType(str) != ObjectToType(int)


def test_eq_not_implemented() -> None:
    ObjectToType(int) != int  # type: ignore
