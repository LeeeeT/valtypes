import pytest

import valtypes.error.parsing.comparison as error
from valtypes import parse_json
from valtypes.type import float


def test_uses_constructor_to_parse_float_to_subclass_of_float() -> None:
    assert parse_json(float.Positive, 2.0) == 2.0

    with pytest.raises(error.ExclusiveMinimum):
        parse_json(float.Positive, 0.0)
