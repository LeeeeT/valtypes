import pytest

import valtypes.error.float as float_error
from valtypes import parse
from valtypes.type import float


def test_uses_constructor_to_parse_float_to_subclass_of_float() -> None:
    assert parse(float.Positive, 2.0) == 2

    with pytest.raises(float_error.ExclusiveMinimum):
        parse(float.Positive, 0.0)
