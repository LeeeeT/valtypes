import pytest

import valtypes.error.parsing as error
from valtypes.parsing.parser import ObjectToType


def test_returns_value_if_its_type_is_correct() -> None:
    assert ObjectToType(int).parse(2) == 2


def test_raises_error_if_value_type_is_wrong() -> None:
    with pytest.raises(error.WrongType) as info:
        ObjectToType(int).parse("2")

    assert info.value == error.WrongType(int, "2")
