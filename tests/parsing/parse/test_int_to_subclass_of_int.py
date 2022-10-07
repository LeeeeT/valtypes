import pytest

import valtypes.error.parsing.type.numeric as error
from valtypes import parse
from valtypes.type import int


def test_uses_constructor_to_parse_int_to_subclass_of_int() -> None:
    assert parse(int.Positive, 2) == 2

    with pytest.raises(error.Minimum):
        parse(int.Positive, 0)
